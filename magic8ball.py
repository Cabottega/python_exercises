import sys
import random

ans = True

while ans:
    question = input("Ask the Magic 8 ball a question (press enter to quit) ")

    answers = random.randint(1, 8)

    if question == "":
        sys.ext()

    elif answers == 1:
        print("It is certain")
    
    elif answers == 2:
        print("Outlook is good")
    
    elif answers == 3:
        print("Rely on it")

    elif answers == 4:
        print("never")
    
    elif answers == 5:
        print("ask again later")
    
    elif answers == 6:
        print("I think you are on to something")
    
    elif answers == 7:
        print("Not happening this year")
    
    elif answers == 8:
        print("Better of next time")

        