from random import randint


def main():
    answers = [
        "Yes - definitely.",
        "It is decidedly so.",
        "Without a doubt.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
    ]
    random_number = randint(0, len(answers) - 1)
    name = input("What is your name?\n")
    question = input("What is your question?\n")
    if len(question) == 0:
        print("No question was asked!")
    elif len(name) == 0:
        print(f"Question: {question}")
        print(f"Magic 8-Ball's answer: {answers[random_number]}")
    else:
        print(f"{name} asks: {question}")
        print(f"Magic 8-Ball's answer: {answers[random_number]}")


if __name__ == "__main__":
    main()
