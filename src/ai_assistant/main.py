from ai_assistant.core.assistant import Assistant
from ai_assistant.config import APP_NAME, VERSION


def main():
    assistant = Assistant(APP_NAME)

    print(APP_NAME)
    print(f"Version: {VERSION}")

    response = assistant.chat("Hello")

    print(response)


if __name__ == "__main__":
    main()