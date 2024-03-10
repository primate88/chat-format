"""Module for formatting chat messages into different formats."""

class Format:
    """Class to format chat messages.

    Attributes:
        allowed_formats (list of str): Permitted formats for output.
    """
    allowed_formats = ["chatml", "llama2", "zephyr"]

    def __init__(self, format_style="chatml", messages=None, add_assistant_prompt=True):
        """Initialize the Format class with default values.

        Args:
            format_style (str): The desired output format. Defaults to "chatml".
            messages (list of dict): Chat messages to format.
            add_assistant_prompt (bool): Flag to add an assistant prompt. Defaults to True.

        Raises:
            ValueError: If add_assistant_prompt is not boolean.
            ValueError: If messages is not a list of dictionaries.
            ValueError: If format_style is not in the allowed formats.
        """
        # Check if add_assistant_prompt is boolean
        if not isinstance(add_assistant_prompt, bool):
            raise ValueError("add_assistant_prompt must be a boolean")
        
        # Check if messages is a non-empty list of dictionaries
        if not messages or \
           not isinstance(messages, list) or \
           not all(isinstance(message, dict) for message in messages):
            raise ValueError("messages must be a non-empty list of dictionaries")
        
        # Convert the format_style to lowercase and check if it's allowed
        format_style = format_style.lower()
        if format_style not in self.allowed_formats:
            raise ValueError(f"The format '{format_style}' is not supported. Choose from {self.allowed_formats}")
        
        # Initialize instance variables
        self.format_style = format_style
        self.messages = messages
        self.add_assistant_prompt = add_assistant_prompt
