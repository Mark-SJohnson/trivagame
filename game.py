print("Welcome to Mark's marvel trivia \nmy name is Mark and I will be your host")

answer = input("Are you ready to play? Yes or No ")

score = 0 

questions = 4


if answer.lower() == "yes":
    answer = input("Question 1: Which avenger is always angry?")
    if answer.lower() == "hulk":
        score += 1
        print("Correct!")
    else:
        print("wrong Answer -_-")

    answer = input("Question 2 Who is the god mischief?")
    if answer.lower() == "loki":
        score += 1
        print(" Correct again your on a roll!") 
    else:
        print("Come on smalls get it together") 

    answer = input("Question 3 Which marvel character had the biggest box office movie?")
    if answer.lower() == "spiderman":
        score += 1
        print("Correct you on Fire")
    else:
        print("Take a lap") 

    answer = input("Question 4 Who is the strongest avenger? ")
    if answer.lower() == "wanda":
        score += 1
        print("Correct I'm impressed")
    else:
        print("Again wrong answer")


print("Your final score is", score * 25,"Have a great day")


         





