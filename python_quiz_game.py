print("Welcome to python quiz!")
want_to_play = input("Type ok if you are ready ")
if want_to_play != "ok":
    print("Well, Goodbye then!")
    quit()
else:
    print("Let's get started!")
points = 0
question1 = input("What year did the world war 2 start? \nA)1939 \nB)1938\nC)1937\nD)1936\nYour answer is: ")
if question1 == "A" or question1 == "a":
    print("Congratulations!")
    points += 1
else:
    print("Sorry, that was wrong")
print(points)