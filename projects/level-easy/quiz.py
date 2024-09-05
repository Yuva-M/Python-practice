print("Howdy all")
print("Do you want to play a quiz?")
score = 0

if input("Enter yes or no: ".lower()) == "yes":
    print("Let's play!")
else:
    print("Maybe next time!")
    quit()   

answer = input("what is the capital of India?")
if answer.lower() == "new delhi".replace(" ", ""):
    print("Correct!")
    score += 1
    print("Your score is", score)
else:
    print("Incorrect!") 

answer = input("what is the capital of England?")
if answer.lower() == "london".replace(" ", ""):
    print("Correct!")
    score += 1
    print("Your score is", score)
else:
    print("Incorrect!") 

answer = input("what is the capital of Brazil?")
if answer.lower() == "brasilia".replace(" ", ""):
    print("Correct!")
    score += 1
    print("Your score is", score)
else:
    print("Incorrect!") 
