from ai_assistant.config import APP_NAME, VERSION
from ai_assistant.core.assistant import Assistant


def main():
    assistant = Assistant(APP_NAME)

    print(APP_NAME)
    print(f"Version: {VERSION}")
    print("-" * 30)

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bye!")
            break

        response = assistant.chat(user_input)

        print(response)
        print()


if __name__ == "__main__":
    main()