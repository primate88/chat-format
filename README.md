# Chat-Format
A Python library designed to effortlessly format JSON chat data for language models, making the development of chat-based applications more intuitive and efficient.

## Features
- **Flexible Formatting:** Supports various chat data formats, including custom structures, to accommodate different language models.
- **Easy Integration:** Simplifies the process of preparing chat data for processing by AI models, saving time and reducing errors.
- **Customizable Outputs:** Offers options to include additional prompts or instructions for the language model, enhancing the quality of interactions.

## Installation
~~To install the Chat-Format library, run the following command in your terminal: `pip install chat-format`~~

## Quick Start
Here's a simple example to get you started with Chat-Format:

```python
from chat_format import FormatPrompt

# Sample chat data
messages = [
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
        "content": "Greetings, Talking Monkey! How can I assist you today?"
    },
    {
        "role": "user",
        "content": "Tell me a joke about bananas."
    }
]

# Formatting the chat data
prompt_formatter = FormatPrompt(
    format="chatml",  # Specify the desired output format
    messages=messages,
    add_assistant_prompt=True  # Include an additional prompt for the assistant
)

formatted_prompt = prompt_formatter.format()
print(formatted_prompt)
```

This code snippet demonstrates how to format a series of chat messages for processing by a language model, making it easier to generate responses or analyze conversations.

## Contributing
If you have suggestions for improvements or bug fixes, please feel free to submit an issue or pull request.

## License
Chat-Format is released under the Apache-2.0 License. See [LICENSE](LICENSE) for more information.
