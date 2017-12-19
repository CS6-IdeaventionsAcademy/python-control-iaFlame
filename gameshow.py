# Tristan
# 11-28-17
# Game Show



print("Welcome to Flame's Game Show!")

print("To win a prize, choose a correct box. But beware, only one box is correct. Other ones will result in complete failure.")

print("So, are you ready to play?")

confirm = input("Do you want to play? ")
if confirm == "yes":
    print("Great let's get started")
else:
    print("Ok bye") 

            
prize1 = "YOU WON A FOOTBALL SIGNED BY CAM NEWTON!"
prize2 = "YOU WON A STICK THAT YOU GET TO CHOOSE FROM OUTSIDE!"
prize3 = "YOU WON A NEW LAMBO *toy*"
prize4 = "YOU WON A HALF EATEN TACO"

while confirm == "yes":
    answer = input("Which box do you choose? ")
    if answer == "box1":
        print(prize1)
    elif answer == "box2":
        print(prize2)
    elif answer == "box3":
        print(prize3)
    elif answer == "box4":
        print(prize4)
    confirm = input("Do you want to play again? ")

print("Thanks for playing!")
