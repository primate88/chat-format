"""Module for formatting chat messages into different formats."""
from chat_format.formats import chatml, llama2, zephyr

class Formatter:
    """Class to format chat messages into specified templates.

    Attributes:
        allowed_formats (list of str): Permitted formats for output.
    """
    allowed_formats = ["chatml", "llama2", "zephyr"]

    def __init__(self, template="chatml", messages=None, add_assistant_prompt=True):
        """Initialize the Formatter class with default values.

        Args:
            template (str): The desired output template. Defaults to "chatml".
            messages (list of dict): Chat messages to format.
            add_assistant_prompt (bool): Flag to add an assistant prompt. Defaults to True.

        Raises:
            ValueError: If add_assistant_prompt is not boolean.
            ValueError: If messages is not a list of dictionaries.
            ValueError: If template is not in the allowed formats.
        """
        # Check if add_assistant_prompt is boolean
        if not isinstance(add_assistant_prompt, bool):
            raise ValueError("add_assistant_prompt must be a boolean")
        
        # Check if messages is a non-empty list of dictionaries
        if not messages or \
           not isinstance(messages, list) or \
           not all(isinstance(message, dict) for message in messages):
            raise ValueError("messages must be a non-empty list of dictionaries")
        
        # Convert the template to lowercase and check if it's allowed
        template = template.lower()
        if template not in self.allowed_formats:
            raise ValueError(f"The template '{template}' is not supported. Choose from {self.allowed_formats}")
        
        # Initialize instance variables
        self.template = template
        self.messages = messages
        self.add_assistant_prompt = add_assistant_prompt
