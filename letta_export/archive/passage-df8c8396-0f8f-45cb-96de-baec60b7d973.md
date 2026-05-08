# Letta API response format â€” messages endpoint (2026-05-08)

*ID: passage-df8c8396-0f8f-45cb-96de-baec60b7d973*
*Created: 2026-05-08*

---

Letta API response format â€” messages endpoint (2026-05-08)

POST /v1/agents/{id}/messages with return_message_object: False returns a DICT, not a list:
  {messages: [...], stop_reason: ..., usage: ..., logprobs: ..., turns: ...}

Each message in the messages array has:
  - message_type: 'reasoning_message' | 'assistant_message' | 'tool_call_message' | etc.
  - content: string (for assistant_message)
  - NOT 'role' field â€” that field does not exist on these objects

To extract the agent's text response:
  msgs = data.get('messages', data) if isinstance(data, dict) else data
  for msg in msgs:
      if msg.get('message_type') == 'assistant_message':
          return msg.get('content', '')

Bug: original code checked isinstance(data, list) â€” always False. Also checked role == 'assistant' â€” field doesn't exist. Result: letta_evaluate() always returned None silently. Fixed 2026-05-08.
