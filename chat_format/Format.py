class Format:
    # Define a class variable with allowed formats
    allowed_formats = ["chatml", "llama2", "zephyr"]

    def __init__(self, format="chatml", messages=None, add_assistant_prompt=True):
        # Check if add_assistant_prompt is boolean
        if not isinstance(add_assistant_prompt, bool):
            raise ValueError("add_assistant_prompt must be a boolean")
        # Check if messages is a non-empty list of dictionaries
        if not messages or not isinstance(messages, list) or not all(isinstance(message, dict) for message in messages):
            raise ValueError("messages must be a non-empty list of dictionaries")
        # Convert the format to lowercase and check if it's allowed
        format = format.lower()
        if format not in self.allowed_formats:
            raise ValueError(f"The format '{format}' is not supported. Choose from {self.allowed_formats}")
        # Initialize instance variables
        self.format = format
        self.messages = messages
        self.add_assistant_prompt = add_assistant_prompt
