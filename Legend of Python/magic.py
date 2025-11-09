import random
print("What is your question")
x = input()
Answers = ["Yes - definitely.", "It is decidedly so.", "Without a doubt.",
           "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
           "My sources say no.", "Outlook not so good.", "Very doubtful."]
print("Question:" + x)
print("Response:"+random.choice(Answers))
