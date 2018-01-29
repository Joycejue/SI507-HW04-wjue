def ask_question():
    question = ""
    while question != "quit":
        question = input("What's your question?(ends with '?')('quit' for quit)")
        if question[-1] == "?":
            return question
        elif question == "quit":
            break
        else:
            input("I'm sorry, I can only answer questions. Ask again.")


ask_question()
