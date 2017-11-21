# Tristan
# 11/15/17
# Python Beginnings
# 6 Password Checker

import time

print("To initiate missile launch sequence, please type your name and password.")

password = ("theresaninfestationinmymindsimaginationihopethattheychokeonsmokecauseimsmokinthemoutthebasementthisisnotrapthisisnothiphopjustanotherattempttomakethevoicesstop")

username = ("Tyler")

name_guess = input("What is your name? ")

if name_guess == username:
    print("Hello Tyler")
    password_guess = input("What is the password? ")

    if password_guess == password:
        print("OMG U REALLY ARE TYLER JOSEPH! TAP THE PERSON TO YOUR RIGHT ON THE SHOULDER TO LAUNCH THE MISSILE!")
    else:
        print("You'll never be Tyler Joseph. Self Destruction Initiating",end='')
        print(".",end='')
        time.sleep(0.4)
        print(".",end='')
        time.sleep(0.4)
        print(".",end='')
  
else:
    print("Self Destruction Initiating",end='')
    print(".",end='')
    time.sleep(0.4)
    print(".",end='')
    time.sleep(0.4)
    print(".",end='')


        
    

