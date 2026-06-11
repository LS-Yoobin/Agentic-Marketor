# Automatic Trading Bot — Design Specification
**Date:** 2026-05-27  
**Owner:** Yoobin  
**Status:** Approved for implementation  

---

## 1. Overview

A safe, sustainable, semi-autonomous swing trading bot for US equities. Built in Python with a modular pipeline architecture where each component has a single responsibility and the safety layer has absolute veto power independent of all AI components.

**Core philosophy:** Deterministic Python logic generates all alpha. Claude acts as a parallel reviewer — never as a signal source and never as a gate. Human approval is required for every trade entry via Telegram before execution. Stop-loss exits are auto-executed without approval (defensive action).

---

## 2. Goals & Constraints

| Goal | Detail |
|---|---|
| Asset class | US equities (stocks) |
| Trading style | Swing trading — holds 2–5 days, daily + 4h candles |
| Universe | 300–500 liquid stocks: S&P 500 + Russell 1000 filter |
| Universe filter | Avg daily volume > 2M shares, market cap > $2B |
| Brokerage | Alpaca Markets (paper trading first, live later) |
| Autonomy | Semi-autonomous — bot signals, human approves entries via Telegram |
| Notifications | Telegram bot + local web dashboard |
| Capital | Paper trading only until 30-day graduation threshold met |
| Language | Python 3.11+ |

**Non-goals (explicitly out of scope):**
- Day trading / intraday signals
- Crypto, forex, options
- Fully autonomous execution (no human approval for entries)
- Predictive price targets from Claude

---

## 3. Architecture — Modular Pipeline

```
DATA PIPELINE
    ↓
INDICATOR ENGINE  (per-stock indicators)
    ↓
UNIVERSE RANKER   (cross-sectional ranking — runs before signal engines)
    ↓
ALPHA SIGNAL 1: MOMENTUM  +  ALPHA SIGNAL 2: MEAN REVERSION  (parallel)
    ↓ (candidate list merged from both signals)
HMM BRAIN — REGIME GATE  (filters candidates by current market state)
    ↓ (regime-approved candidates)
    ├──→ CLAUDE ANALYST  (parallel annotation — risk score added to card, does NOT gate)
    ↓
RISK MANAGER — ABSOLUTE VETO  (position sizing, circuit breakers)
    ↓ (risk-approved signals)
TELEGRAM APPROVAL — human /approve or /reject  (entries only)
    ↓ (if approved)
ALPACA BROKER  ←──→  DASHBOARD  (execution + real-time display)
```

**Claude's position in the pipeline:** Claude runs in parallel after the Regime Gate — it annotates each candidate with a risk score that appears on the Telegram card. It does NOT block execution. The Risk Manager is the only component that can veto a trade.

### Project Structure

```
trading-bot/
├── .env                      ← secrets (never committed to git)
├── .gitignore                ← includes .env, data/cache/, *.db, .trading.lock
├── .trading.lock             ← written by circuit breaker; delete manually to restart
├── main.py                   ← orchestrator — runs the daily pipeline in sequence
├── config/
│   ├── settings.yaml         ← all tuneable parameters (periods, thresholds, limits)
│   └── watchlist.yaml        ← 300–500 ticker symbols with GICS sector tags
├── data/
│   ├── fetcher.py            ← Alpaca API: OHLCV, VIX, SPY, sector ETFs
│   ├── cleaner.py            ← NaN removal, OHLCV validation, breadth calculation
│   ├── sector_map.py         ← loads GICS sector from watchlist.yaml for each ticker
│   └── cache/                ← Parquet files (gitignored)
├── indicators/
│   ├── t3.py                 ← T3 moving average: small (8), mid (21), large (55)
│   ├── divergence.py         ← RSI-14 / MACD divergence detection
│   ├── background_color.py   ← trend score per bar → green / grey / red zones
│   ├── volume_breakout.py    ← price > swing high + volume > 1.5× 20d avg
│   ├── atr_sizing.py         ← ATR-14: stop distance, target, share count
│   ├── rsi_percentile.py     ← RSI-14 rank vs. rolling 252-day window
│   └── relative_strength.py  ← 1m, 3m, 6m return vs. SPY
├── universe/
│   └── ranker.py             ← cross-sectional ranking: momentum score + RS rank
├── regime/
│   ├── hmm_engine.py         ← hmmlearn HMM, 5 states, trained on SPY features
│   ├── stability_filter.py   ← requires 3+ consecutive daily bars in same state
│   └── macro_gate.py         ← VIX threshold + market breadth check
├── signals/
│   ├── momentum.py           ← Alpha 1: Rules 1, 2, 3 using ranked universe
│   └── mean_reversion.py     ← Alpha 2: oversold dip on a strong stock
├── analyst/
│   └── claude_reviewer.py    ← Claude API, reviewer only, returns risk score JSON
├── risk/
│   ├── risk_manager.py       ← position sizing, sector check, veto logic
│   ├── circuit_breakers.py   ← daily loss monitor (–3%), drawdown monitor (–10%)
│   └── lock_file.py          ← write/check/clear .trading.lock in project root
├── notifications/
│   └── telegram_bot.py       ← async polling, /approve_TICKER_UUID, /reject_TICKER_UUID
├── broker/
│   └── alpaca_client.py      ← order placement, stop monitoring, position management
├── backtest/
│   ├── walk_forward.py       ← rolling train/test engine
│   ├── stress_test.py        ← injects historical crash windows
│   └── metrics.py            ← Sharpe, max drawdown, profit factor, consistency score
├── dashboard/
│   ├── app.py                ← FastAPI app, serves on http://localhost:8080
│   ├── templates/            ← Jinja2 HTML (live.html, signals.html, backtest.html, risk.html, history.html)
│   └── static/               ← CSS, JS
└── database/
    └── trades.db             ← SQLite: signal log, trade history, Claude review log
```

---

## 4. Component Specifications

### 4.1 Data Pipeline (`data/`)

**Source:** Alpaca Markets API  
**Cadence:** Automated fetch once per day, 30 minutes before market open (9:00 AM ET)  

| Data | Timeframe | History | Purpose |
|---|---|---|---|
| OHLCV for all watchlist tickers | Daily | 3 years | Indicators, HMM training, backtest |
| OHLCV for all watchlist tickers | 4h | 6 months | Signal confirmation |
| VIX index (^VIX) | Daily | 3 years | Macro gate threshold |
| SPY (S&P 500 ETF) | Daily | 3 years | Breadth calc, HMM features, RS baseline |
| Sector ETFs (XLK, XLF, XLE, XLV, XLI, XLY, XLP, XLU, XLB, XLRE, XLC) | Daily | 1 year | Sector flow context for dashboard |

**Market breadth definition:**  
Breadth = (number of watchlist stocks with close > 200-day SMA) / (total watchlist stocks)  
Macro gate closes when breadth < 0.40 (fewer than 40% of stocks are in a long-term uptrend).

**GICS sector data:**  
Stored in `config/watchlist.yaml` — each ticker entry includes its GICS sector tag. Loaded by `data/sector_map.py`. No live fetch required; updated manually when watchlist changes.

**Cleaning rules:**  
- Drop rows where any OHLCV field is NaN  
- Validate: Open ≤ High, Low ≤ Close, Low ≤ Open, Volume > 0  
- Forward-fill up to 1 missing bar (handles exchange holidays)  

**Storage:** Parquet files in `data/cache/{ticker}_{timeframe}.parquet` — fast columnar reads, gitignored.

---

### 4.2 Indicator Engine (`indicators/`)

All indicators are pure Python (pandas + numpy). No chart images sent to Claude. Every formula is unit-testable in isolation.

#### T3 Moving Average — `t3.py`
Tim Tillson's T3: a smooth, lag-reduced moving average built from 6 successive EMAs.  
Parameters (stored in `config/settings.yaml`):

| Band | Period | vFactor |
|---|---|---|
| Small | 8 | 0.7 |
| Mid | 21 | 0.7 |
| Large | 55 | 0.7 |

Output columns per ticker: `t3_small`, `t3_mid`, `t3_large`

#### Divergence Lines — `divergence.py`
RSI-14 divergence (bearish and bullish).  
- **Bearish divergence:** Price makes higher high, RSI-14 makes lower high (within a 20-bar lookback window)  
- **Bullish divergence:** Price makes lower low, RSI-14 makes higher low (within a 20-bar lookback window)  
- Peak/trough detection: local extrema within ±3 bars  
Output columns: `bearish_divergence` (bool), `bullish_divergence` (bool)  
**Used by:** Mean Reversion signal (bullish divergence on dip = stronger signal)

#### Background Color Logic — `background_color.py`
Trend score per bar using 3 conditions:
1. Close > T3 large (bullish)
2. T3 small > T3 mid (short-term momentum up)
3. T3 mid > T3 large (medium-term momentum up)

Scoring:
- 3/3 conditions true → `GREEN` (strong uptrend)
- 2/3 conditions true → `LIGHT_GREEN`
- 1/3 conditions true → `GREY` (ranging)
- 0/3 conditions true → `RED` (downtrend)

Output column: `bg_color` (enum: GREEN, LIGHT_GREEN, GREY, RED)  
**Used by:** Momentum Rule 2 (requires GREEN or LIGHT_GREEN for Clear Path)

#### Volume-Confirmed Breakout — `volume_breakout.py`
- Swing high: rolling 20-bar maximum of daily highs  
- Breakout: current close > prior bar's swing high  
- Volume condition: current volume > 1.5 × 20-day average volume  
- Signal fires only when both conditions true on the same bar  
Output column: `vol_breakout` (bool)

#### ATR-Based Sizing — `atr_sizing.py`
Uses ATR-14 (14-period Average True Range).  
- Stop distance: 2 × ATR-14 below entry price  
- Target distance: stop distance × 1.5 (minimum 1.5:1 reward-to-risk)  
- Share count: `floor((portfolio_value × risk_pct) / stop_distance_dollars)`  
Output columns: `atr14`, `stop_price`, `target_price`, `share_count`

#### RSI Percentile Rank — `rsi_percentile.py`
Base RSI period: **14** (standard).  
Percentile rank: position of today's RSI-14 within its own rolling 252-day (1 year) window.  
`rsi_pct_rank = percentileofscore(rsi_14[-252:], rsi_14[-1])`  
Output column: `rsi_pct_rank` (0–100)

#### Relative Strength vs. SPY — `relative_strength.py`
For each ticker, compute return over 1-month (21 bars), 3-month (63 bars), 6-month (126 bars), then subtract SPY return over the same window.  
`rs_score = (rs_1m + rs_3m + rs_6m) / 3`  
Output column: `rs_score` (float, positive = outperforming SPY)

---

### 4.3 Universe Ranker (`universe/ranker.py`)

Runs once per day after all indicators are computed, before any signal engine.  
Computes a cross-sectional momentum rank for every stock in the universe:

```
momentum_rank = rank(12-1 month return)   # 12-month return minus last month
rs_rank       = rank(rs_score)            # relative strength vs. SPY
combined_rank = (momentum_rank + rs_rank) / 2
```

Ranking is percentile-based (0–100, 100 = best). Top 20% combined rank = `top_quintile = True`.  
This rank is used by the Momentum signal (Rule 1 requires `top_quintile = True`).

---

### 4.4 Dual Alpha Signals (`signals/`)

#### Alpha 1 — Momentum (`signals/momentum.py`)

Buys stocks in confirmed uptrends with strong relative performance.

| Rule | Condition | Data source |
|---|---|---|
| Rule 1 — Momentum | `top_quintile == True` (top 20% of universe by combined rank) | `universe/ranker.py` |
| Rule 2 — Clear Path | `bg_color in [GREEN, LIGHT_GREEN]` AND no swing high within 3% above entry | `background_color.py`, `volume_breakout.py` |
| Rule 3 — Entry | `vol_breakout == True` on daily close | `volume_breakout.py` |

All 3 rules must be true simultaneously. Output: candidate dict with ticker, entry price, stop, target, signal type = `MOMENTUM`.

Active regimes and size multipliers:
- Euphoria: 0.6× normal size
- Bull: 1.0× normal size
- Neutral: 0.5× normal size
- Bear / Crash: disabled

#### Alpha 2 — Mean Reversion (`signals/mean_reversion.py`)

Buys fundamentally strong stocks that have temporarily pulled back.

| Condition | Threshold | Data source |
|---|---|---|
| Oversold | `rsi_pct_rank < 20` | `rsi_percentile.py` |
| Structure intact | `close > t3_large` | `t3.py` |
| Volume contracting | Last 3 bars all have volume < 20-day avg volume | `fetcher.py` |
| Bullish divergence (bonus) | `bullish_divergence == True` (not required, but boosts Claude risk score) | `divergence.py` |

All first 3 conditions must be true. Output: candidate dict with ticker, entry price, stop, target, signal type = `MEAN_REVERSION`.

Active regimes:
- Bull: 1.0× normal size
- Neutral: 0.5× normal size
- Euphoria: 0.5× normal size
- Bear / Crash: disabled

#### Why These Are Uncorrelated
Momentum profits when markets trend upward continuously. Mean Reversion profits when strong stocks have brief pullbacks. During momentum crashes (Aug 2015, Q4 2018, Mar 2020) mean-reversion signals often activate — the strategies partially offset each other across market cycles. The Risk Manager tracks total exposure per signal type separately.

---

### 4.5 HMM Brain & Regime Gate (`regime/`)

**Model:** Hidden Markov Model (`hmmlearn.GaussianHMM`)  
**States:** 5 — Crash, Bear, Neutral, Bull, Euphoria  
**Training features** (SPY daily):  
- Log returns: `log(close / close.shift(1))`  
- Rolling 20-day volatility (z-scored): `std(log_returns[-20:]) - mean / std` over full history  

**Training:** On first run, trains on all available SPY history (3 years minimum). Retrains weekly.  
**Prediction:** Most probable state for today's bar via Viterbi algorithm.

**Stability filter (`stability_filter.py`):**  
State must appear for ≥ 3 consecutive daily bars before the regime gate changes state. Prevents over-trading on flickering signals.

**Macro gate (`macro_gate.py`) — runs first, before HMM result is used:**  

| Condition | Threshold | Action |
|---|---|---|
| VIX | > 30 | Gate closes — all signals disabled regardless of regime |
| Market breadth | < 0.40 | Gate closes — all signals disabled regardless of regime |

If macro gate closes: log reason, send Telegram notification "⚠️ Macro gate closed — no trades today", skip signal engines.

**Regime → position size multiplier table:**

| Regime | Momentum | Mean Reversion |
|---|---|---|
| Crash | ❌ 0× | ❌ 0× |
| Bear | ❌ 0× | ❌ 0× |
| Neutral | ✅ 0.5× | ✅ 0.5× |
| Bull | ✅ 1.0× | ✅ 1.0× |
| Euphoria | ✅ 0.6× | ✅ 0.5× |

---

### 4.6 Walk-Forward Backtest (`backtest/`) — Required Gate Before Paper Trading

**Trigger:** Run manually once via `python backtest/walk_forward.py`. Writes a pass/fail report to `backtest/results/report_YYYY-MM-DD.json`. Paper trading will not run until a passing report exists.

**Method:** Rolling expanding train window, fixed 6-month test window:
- Train: all data from start → window end
- Test: next 6 months (out-of-sample, strict time order)
- Slide: advance test window by 6 months, repeat until end of data

**Both alpha signals tested:** independently and combined.

**Transaction costs (baked in to every simulated trade):**
- Commission: $0.005 per share  
- Slippage: 10 basis points (0.10%) per trade  
- No partial fills assumed (full fill at next open)

**Stress periods (tagged and reported separately):**
- COVID crash: 2020-02-19 → 2020-04-30
- Rate hike bear: 2022-01-01 → 2022-12-31
- Q4 2018 correction: 2018-10-01 → 2018-12-31
- Aug 2015 momentum crash: 2015-08-01 → 2015-09-30

**Pass gates (all 4 must be met before `main.py` allows paper trading to start):**

| Metric | Required threshold |
|---|---|
| Annualised Sharpe ratio | > 0.8 |
| Maximum drawdown | < 20% |
| Profit factor (gross profit / gross loss) | > 1.3 |
| Window consistency | Positive Sharpe in ≥ 70% of test windows |

**On failure:** Report written with which gates failed. `main.py` logs "Backtest not passed — paper trading locked" and exits. No manual override — fix the strategy, re-run.

**30-day paper trading graduation criteria (for live capital approval):**
- 30 consecutive trading days completed
- Rolling Sharpe > 1.0 over the 30 days
- No circuit breaker triggered
- Maximum drawdown < 10% over the 30 days

---

### 4.7 Claude Analyst (`analyst/`) — Parallel Reviewer

**Position in pipeline:** Runs in parallel after regime gate, annotates each candidate. Does NOT gate execution — Risk Manager has that role exclusively.

**Input schema (JSON passed to Claude API):**
```json
{
  "ticker": "NVDA",
  "signal_type": "MOMENTUM",
  "regime": "BULL",
  "entry_price": 127.40,
  "stop_price": 122.80,
  "target_price": 136.20,
  "rs_score": 0.12,
  "rsi_pct_rank": 72,
  "bg_color": "GREEN",
  "vol_breakout": true,
  "bullish_divergence": false,
  "days_to_next_earnings": 43
}
```

**System prompt (cached):** "You are a risk reviewer for a systematic trading bot. You do not generate trade ideas. For each candidate trade presented, identify risks the systematic rules may have missed. Focus on: earnings risk, sector headwinds, macro context, and any reason the setup might fail. Return a JSON object only."

**Output schema (stored in `trades.db`):**
```json
{
  "ticker": "NVDA",
  "risk_level": "LOW",
  "summary": "No earnings for 6 weeks. Sector breadth strong. No divergence flags.",
  "flags": []
}
```

**Model:** `claude-sonnet-4-6` via Anthropic SDK with prompt caching on system prompt.  
**Failure handling:** If Claude API call fails, trade proceeds with `risk_level: "UNKNOWN"` — Claude annotation is non-blocking.

---

### 4.8 Risk Manager (`risk/`) — Absolute Veto

The Risk Manager is the only component that can prevent a trade from reaching the Telegram approval step. It has no dependency on Claude output.

**Position sizing formula:**
```
stop_distance = entry_price - stop_price   (from atr_sizing.py)
max_risk_dollars = portfolio_value × 0.01  (1% of portfolio)
shares = floor(max_risk_dollars / stop_distance)
notional = shares × entry_price
```

**Position limits (veto conditions — any one fails = trade blocked):**

| Limit | Value |
|---|---|
| Max simultaneous momentum positions | 3 |
| Max simultaneous mean-reversion positions | 2 |
| Max positions in same GICS sector | 1 |
| Max single position notional | 20% of portfolio value |

**Circuit breakers (`circuit_breakers.py`) — hardcoded, AI-independent:**

| Trigger | Calculation | Action |
|---|---|---|
| Daily loss –3% | (portfolio_value_now – portfolio_value_at_prior_close) / portfolio_value_at_prior_close < –0.03 | Close all open positions via market orders immediately |
| Peak drawdown –10% | (portfolio_value_now – all_time_high_since_start) / all_time_high_since_start < –0.10 | Write `.trading.lock`, close all positions, shut down bot |

**Lock file (`lock_file.py`):**
- Path: `{project_root}/.trading.lock`
- Contents: timestamp + trigger reason + portfolio value at trigger
- Checked at every `main.py` startup — if file exists, bot logs error and exits immediately
- Pending Telegram approvals: any trades in "awaiting approval" state are auto-rejected with message "⚠️ Trading locked — circuit breaker triggered. Review required."
- Cleared only by manual deletion: `del .trading.lock` — this forces human review

---

### 4.9 Telegram Approval (`notifications/`)

**Library:** `python-telegram-bot` v20+ (async, ApplicationBuilder pattern)  
**Connection:** Long polling — no public server, no domain, no SSL required. Runs locally.  
**Config:** Bot token from `.env → TELEGRAM_BOT_TOKEN`. Whitelisted user ID from `.env → TELEGRAM_USER_ID`. All messages from other user IDs are silently ignored.

**Trade ID format:** UUID4 generated at signal creation. Stored in `trades.db`. Telegram commands use first 8 chars: `/approve_NVDA_a1b2c3d4`.

**Trade alert message format:**
```
🤖 TRADE SIGNAL — MOMENTUM
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ticker:    NVDA
Entry:     $127.40
Stop:      $122.80  (ATR ×2, –3.6%)
Target:    $136.20  (1.5:1 R:R)
Shares:    42  |  Risk: $184  (0.9%)

Regime:    🟢 BULL
Claude:    🟢 LOW RISK — No earnings 6 weeks.
           Sector breadth strong. No divergence.

⏱ Expires in 30 min
/approve_NVDA_a1b2c3d4   /reject_NVDA_a1b2c3d4
```

**Approval flow:**
1. `/approve_NVDA_a1b2c3d4` → Risk Manager re-checks current positions (30min may have passed) → if still valid, Alpaca market order placed → confirmation sent to Telegram
2. `/reject_NVDA_a1b2c3d4` → logged as `USER_REJECTED` in `trades.db`, no execution
3. No response within 30 min → logged as `EXPIRED`, no execution

**Stop-loss exits:** Auto-executed by `broker/alpaca_client.py` without Telegram approval — exits are defensive and should not require human confirmation. A Telegram notification is sent *after* the exit executes: "🔴 Stop hit — NVDA exited at $122.65. P&L: –$184."

---

### 4.10 Broker Integration (`broker/alpaca_client.py`)

**API:** Alpaca Markets (`alpaca-py` library)  
**Mode:** Controlled by `ALPACA_PAPER=true` in `.env` — switches between paper and live endpoints  
**Order type:** Market orders placed at next market open after Telegram approval  
**Stop monitoring:** Runs at 9:35 AM ET daily (5 min after open) using prior-day close data. For each open position, checks if close < stop_price. If yes, submits market sell order immediately (no approval needed).

---

### 4.11 Dashboard (`dashboard/`)

**Stack:** FastAPI + Jinja2 templates + vanilla JS with auto-refresh every 60 seconds  
**Access:** Local only, `http://localhost:8080`  
**Data source:** All pages read from `database/trades.db` and live Alpaca API calls

| Page | URL | Content |
|---|---|---|
| **Live** | `/` | Current regime + macro gate status, open positions with live P&L, today's circuit breaker level (current drawdown vs. –3% and –10% thresholds) |
| **Signals** | `/signals` | Pending Telegram approvals, last 50 signals generated (ticker, signal type, rules that fired, Claude risk score, outcome) |
| **Backtest** | `/backtest` | Walk-forward results: Sharpe per window chart, max drawdown, profit factor, stress period breakdown. Pass/fail gate status. |
| **Risk** | `/risk` | Active positions by sector (correlation heatmap), lock file status, circuit breaker history |
| **History** | `/history` | All closed trades: entry/exit date, ticker, signal type, regime at entry, P&L, Claude risk score at time of trade |

---

## 5. Secrets & Environment Variables

All secrets stored in `.env` — **never committed to git**.

```
# .env — local machine only
TELEGRAM_BOT_TOKEN=...        # from BotFather
TELEGRAM_USER_ID=...          # your numeric Telegram user ID
ALPACA_API_KEY=...            # from Alpaca dashboard
ALPACA_SECRET_KEY=...         # from Alpaca dashboard
ALPACA_PAPER=true             # set to false only when graduating to live
ANTHROPIC_API_KEY=...         # from Anthropic console
```

`.gitignore` must include:
```
.env
.trading.lock
data/cache/
database/trades.db
backtest/results/
__pycache__/
*.pyc
```

---

## 6. Tech Stack

| Component | Library / Version |
|---|---|
| Language | Python 3.11+ |
| HMM Brain | `hmmlearn` |
| Indicators | `pandas`, `numpy` |
| Broker | `alpaca-py` |
| Claude Analyst | `anthropic` SDK (prompt caching on system prompt) |
| Telegram | `python-telegram-bot` v20+ |
| Dashboard | `FastAPI`, `Jinja2`, `uvicorn` |
| Database | `sqlite3` (stdlib) |
| Data cache | `pyarrow` (Parquet) |
| Config | `pyyaml`, `python-dotenv` |
| Testing | `pytest` |

---

## 7. Build Phases & Gates

| Phase | Deliverable | Gate to next phase |
|---|---|---|
| 1 | Scaffolding: `.env`, `.gitignore`, `config/`, `data/` pipeline | All tickers in watchlist fetch successfully; Parquet files written |
| 2 | All 7 indicators in `indicators/` + `universe/ranker.py` | Each indicator has passing `pytest` unit tests with known input/output |
| 3 | HMM Brain (`regime/`) + both alpha signals (`signals/`) | Regime classifies SPY correctly on 2020 COVID and 2022 bear data |
| 4 | Walk-forward backtest (`backtest/`) | Passes all 4 gates: Sharpe >0.8, drawdown <20%, profit factor >1.3, 70% consistency |
| 5 | Claude Analyst (`analyst/`) | Claude review runs without errors; output stored correctly in `trades.db` |
| 6 | Risk Manager + circuit breakers (`risk/`) | Unit tests: veto fires correctly; lock file created/detected; daily loss trigger tested with mock data |
| 7 | Telegram bot (`notifications/`) | `/approve` and `/reject` tested end-to-end in paper mode; 30-min expiry tested |
| 8 | Dashboard (`dashboard/`) | All 5 pages render with real data from trades.db |
| 9 | 30-day paper trading | Review: Sharpe >1.0, no circuit breaker, drawdown <10% → graduate to live |

---

## 8. Safety Principles (Non-Negotiable)

1. **Risk Manager has absolute veto** — no trade entry executes without Risk Manager sign-off, regardless of signal strength, Claude output, or Telegram approval
2. **Claude never generates alpha** — all buy/sell logic lives in deterministic Python; Claude only annotates after the fact
3. **Claude is non-blocking** — a Claude API failure never stops a trade; the risk score shows as UNKNOWN and the trade proceeds to Telegram
4. **Lock file = mandatory human review** — a –10% drawdown writes `.trading.lock`; the bot refuses to start until it is manually deleted
5. **Stop exits are automatic** — stop-loss hits are executed without human approval (defensive action); Telegram is notified after the fact
6. **Paper trade for 30 days minimum** — no live capital until Sharpe >1.0, no circuit breakers, drawdown <10% over the full 30-day period
7. **`.env` never committed** — all API keys and tokens live in environment variables; `.gitignore` enforced from Phase 1
