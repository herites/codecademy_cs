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
    random_number = randint(0, 8)
    name = input("What is your name?\n")
    question = input("What is your question?\n")
    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answers[random_number]}")


if __name__ == "__main__":
    main()
