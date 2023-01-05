from revChatGPT.ChatGPT import Chatbot

def chatgpt_chat(conversation_id = None):
    chatbot = Chatbot({
    "session_token": ""
    }, conversation_id, parent_id=None) # You can start a custom conversation

    while True:
        user_input = input("Your input: ")
        if user_input.lower() == 'q':
            return
        try:
            response = chatbot.ask(user_input) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)
            print(f"ChatGPT: {response['message']}\n")
        except Exception:
            print("Something just went wrong. Please wait and try again later.")

if __name__ == '__main__':
    chatgpt_chat()