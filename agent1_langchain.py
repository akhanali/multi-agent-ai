from shared.a2a_protocol import send_message



def main():
    print("Welcome to LangChain Agent.")
    while True:
        question = input("Ask something (or 'exit'): ")
        if question.lower() == "exit":
            break
        message = {
            "sender": "langchain-agent",
            "receiver": "llamaindex-agent",
            "content": question
        }
        print("Sending message...")
        response = send_message(message)
        print("Response from LlamaIndex Agent:", response)

if __name__ == "__main__":
    main()
