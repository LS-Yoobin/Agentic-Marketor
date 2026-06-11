import anthropic

SYSTEM_PROMPT = """You are Jarvis, a highly capable personal AI assistant.
You speak in a concise, professional British tone — helpful, direct, never verbose.
You have tools to control Spotify, send emails, open apps, type text, and more.
Always use a tool if the user's request maps to one. Keep responses under 2 sentences."""

MAX_HISTORY = 12  # 6 exchanges


class Brain:
    def __init__(self, api_key: str, tool_registry: dict):
        self._client = anthropic.Anthropic(api_key=api_key)
        self._tools = tool_registry["functions"]
        self._schemas = tool_registry["schemas"]
        self._history: list[dict] = []

    def process(self, user_text: str) -> str:
        self._history.append({"role": "user", "content": user_text})
        if len(self._history) > MAX_HISTORY:
            self._history = self._history[-MAX_HISTORY:]

        response = self._client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            tools=self._schemas,
            messages=list(self._history),
        )

        if response.stop_reason == "tool_use":
            return self._handle_tool_use(response)

        reply = next(b.text for b in response.content if b.type == "text")
        self._history.append({"role": "assistant", "content": reply})
        return reply

    def _handle_tool_use(self, response) -> str:
        tool_block = next(b for b in response.content if b.type == "tool_use")
        tool_fn = self._tools.get(tool_block.name)

        try:
            tool_result = tool_fn(**tool_block.input) if tool_fn else "Tool not available."
        except Exception as e:
            tool_result = f'{{"error": "{str(e)}"}}'

        followup_messages = self._history + [
            {"role": "assistant", "content": response.content},
            {"role": "user", "content": [{
                "type": "tool_result",
                "tool_use_id": tool_block.id,
                "content": str(tool_result)[:200],
            }]}
        ]

        followup = self._client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=512,
            system=SYSTEM_PROMPT,
            tools=self._schemas,
            messages=followup_messages,
        )

        reply = next(b.text for b in followup.content if b.type == "text")
        # Only store clean exchange in history (not tool call internals)
        self._history.append({"role": "assistant", "content": reply})
        return reply
