# chat-format
A tool to format JSON chat data for language models.

## example usage

```
from chat-template import FormatPrompt

chat = [
    {
        "role": "system",
        "content": "You are a friendly ChatBot."
    },
    {
        "role": "user",
        "content": "Hello!"
    },
    {
        "role": "assistant",
        "content": "Greetings, primate! How can I help you today?"
    },
    {
        "role": "user",
        "content": "Tell me a joke about bananas."
    }
]

prompt = FormatPrompt(
    format="chatml",
    messages=messages,
    add_assistant_prompt=True
)

print(prompt)
```
