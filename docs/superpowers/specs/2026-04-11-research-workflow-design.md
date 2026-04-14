# Research Workflow — Design Spec
*2026-04-11*

## Problem

The user needs a reusable, repeatable process for researching any topic and producing a clean, structured report. Without a defined workflow, research quality is inconsistent — sometimes too shallow, sometimes poorly structured, and often missing actionable output.

## Goals

- Agent always asks clarifying questions before researching (scope, audience, intent)
- Number of intake questions adapts to topic complexity
- Research is deep (20+ sources) and multi-layered
- Output is a clean, consistently structured markdown report
- Reports are useful for personal use, team sharing, AND public publishing

## Non-Goals

- Automated scheduling or recurring research
- Integration with external tools (Notion, Google Docs, etc.)
- Multiple output formats (PDF, HTML) — markdown only

## Design

### Approach

Modular 4-phase workflow stored as a plain-english instruction file at `Workflows/research.md`. The agent reads and follows this file when triggered.

### Phase 1: INTAKE
Adaptive clarifying questions — 3 for simple topics, up to 6 for complex. Questions are asked one at a time. Core questions: scope, audience, intent. Extended questions: prior knowledge, recency needs, format preferences.

### Phase 2: RESEARCH
Deep research targeting 20+ distinct sources across 4 coverage layers: foundational context, current landscape, multiple angles (including criticism), and data/statistics. Self-check criteria before proceeding.

### Phase 3: SYNTHESIS
Internal organization of findings by theme. Identifies top 3-5 insights, flags contradictions and gaps, determines optimal section order for the stated audience and intent.

### Phase 4: OUTPUT
Structured markdown report with 8 sections:
1. Executive Summary
2. Background
3. Current Landscape
4. Key Findings (3-6 thematic sub-sections)
5. Contradictions & Open Questions
6. Key Takeaways (5-7 bullets)
7. Recommended Next Steps (3-5 actions)
8. Sources

Report saved to: `output/research-[topic-slug]-YYYY-MM-DD.md`

## Files

- **Workflow:** `Workflows/research.md`
- **Output destination:** `output/`

## Verification

1. Trigger with: *"Run the research workflow on [complex topic]"*
2. Confirm adaptive intake questions fire (4-6 for complex topics)
3. Confirm final report has all 8 sections
4. Confirm report saves to correct path with correct filename format
5. Confirm 20+ sources in the Sources section
