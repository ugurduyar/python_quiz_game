print("Welcome to python quiz!")
want_to_play = input("Type ok if you are ready ")
if want_to_play != "ok":
    print("Well, Goodbye then!")
    quit()
else:
    print("Let's get started!\n")
points = 0
question_count = 0
question = input("What year did the world war 2 start? \nA)1939 \nB)1938\nC)1937\nD)1936\nYour answer is: ")
if question.lower() == "a":
    print("Congratulations!\n")
    points += 1
else:
    print("Sorry, that was wrong\n")
print("You have {} points!\n".format(points))
question_count += 1
question = input("Who first discovered America? \nA)Leif Erikson \nB)Christopher Columbus\nC)Paria Peninsula\nD)William Bradford\nYour answer is: ")
if question.lower() == "a":
    print("Congratulations!\n")
    points += 1
else:
    print("Sorry, that was wrong\n")
print("You have {} points!\n".format(points))
question_count += 1
question = input("When did the American Civil War end? \nA)1845 \nB)1855\nC)1865\nD)1875\nYour answer is: ")
if question.lower() == "c":
    print("Congratulations!\n")
    points += 1
else:
    print("Sorry, that was wrong\n")
print("You have {} points!\n".format(points))
question_count += 1
question = input("Who invented the first car? \nA)Henry Ford \nB)Nicolas-Joseph Cugnot\nC)George B. Selden\nD)Karl Benz\nYour answer is: ")
if question.lower() == "d":
    print("Congratulations!\n")
    points += 1
else:
    print("Sorry, that was wrong\n")
print("You have {} points!\n".format(points))
question_count += 1
question = input("NATO was formed in ... \nA)1949 \nB)1945\nC)1952\nD)1941\nYour answer is: ")
if question.lower() == "a":
    print("Congratulations!\n")
    points += 1
else:
    print("Sorry, that was wrong\n")
print("You have {} points!\n".format(points))
question_count += 1
print("Congratulations! You did {} out of {} \n".format(points,question_count))
print("You did {} percent right\n".format(round((points/question_count)*100)))
input("Thanks for playing!")