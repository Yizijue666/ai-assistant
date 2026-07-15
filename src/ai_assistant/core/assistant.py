class Assistant:

    def __init__(self, name="AI Assistant"):
        self.name = name

    def chat(self, message):
        return f"{self.name} received: {message}"