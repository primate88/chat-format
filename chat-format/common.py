class chat-format:
    def __init__(self):
        self.templates = {
            "chatml": self._chatml_template,
        }
        
    def _chatml_template(self, chat):
        formatted_chat = ""
        for msg in chat:
            role_map = {
                "system": "system",
                "user": "user",
                "assistant": "assistant",
                "instruction": "system",
                "instructions": "system",
                "ape": "user",
                "human": "user",
                "person": "user",
                "ai": "assistant",
                "bot": "assistant",
                "chatbot": "assistant",
                "model": "assistant",
            }

            # Resolve alternative keys for role and content
            role = role_map.get(msg.get("role", msg.get("from", msg.get("speaker", ""))))
            content = msg.get("content", msg.get("message", msg.get("value", "")))
            formatted_chat += f"<|im_start|>{role}\n{content}<|im_end|>\n"
        return formatted_chat

    def apply_chat_template(self, chat, template="chatml", add_generation_prompt=False):
        if template.lower() not in self.templates:
            raise ValueError("Unsupported format passed.")
        
        formatted_chat = self.templates[template.lower()](chat)
        
        if add_generation_prompt:
            if template == "chatml":
                formatted_chat += "<|im_start|>assistant\n"
        
        return formatted_chat
