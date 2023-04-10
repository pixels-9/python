# A 20 question quiz where you have 3 attempts for each question.

questions = {"Who was the first president of the United States?": "George Washington.",
            "What year was the Battle of Hastings?": "1066.",
            "Who was the first soviet leader?": "Vladimir Lenin.",
            "What street did the Fire of London start on?": "Pudding Lane.",
            "What is the capital of England?": "London.",
            "What country is inside the Republic of South Africa?": "Lesotho.",
            "What is the capital of the Australia?": "Canberra.",
            "Where is the island of Madagascar in relation to Mozambique?": "East.",
            "What is the chemical symbol for iron?": "Fe.",
            "What is the name of the largest organ in the human body?": "Skin.",
            "What is the common name for dihydrogen monoxide?": "Water.",
            "Can energy leave a system?": "Yes.",
            "What is a CPU?": "Central Processing Unit.",
            "What is the name of the programming language that is most popular": "Python.",
            "Who invented the first programming language?": "Ada Lovelace.",
            "What is the name of Microsoft's first operating system?": "MS-DOS.",
            "What is the name of the first book of the Bible?": "Genesis.",
            "What is the name of the islamic prophet?": "Muhammad.",
            "What is the name of the sikhs holy book?": "Guru Granth Sahib.",
            "What is the name of the first book of the Torah?": "Genesis."}

def main():
    score = 0
    print("Welcome to the quiz game!\nYou will be asked 20 questions and you will have 3 attempts for each questions.\n" +
          "This test is unforgiving, so remember to capitalise your answers, and don't forget to use punctuation.\n")
    for question in questions:
        print(question)
        for i in range(3):
            answer = input("Answer: ")
            if answer == questions[question]:
                print("Correct!")
                score += 1
                break
            else:
                print("Incorrect! You have " + str(2 - i) + " attempts left.")
    print("You got " + str(score) + " out of 20 questions correct.\n That's " + str(score / 20 * 100) + "%.")
     
    if input("Would you like to play again? (y/n): ") == "y":
        main()

main()