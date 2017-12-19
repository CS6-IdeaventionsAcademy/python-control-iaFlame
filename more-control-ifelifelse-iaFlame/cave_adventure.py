# Tristan Kang
# 12-5-17
# Cave Adventure
# A text-based adventure game

def left_cave():
    # Left cave
    print("You walk into the left cave. It is cold and dark")
    # River Choice
    print("You see an underground river with a boat next to it.")
    print("Do you want to swim, take the boat, or walk along the side?")
    river_choice = input("Type B for (BOAT), S for (SWIM), or W for (WALK): ").upper()
    return river_choice

def right_cave():
    # Right cave
    print("You walk into the right cave. ")
    print("The cave starts sloping downward.")
    # River Choice
    print("You see an a hole with a rope going down and a torch off in the distace.")
    print("Do you want to walk to the torch or climb down the rope?")
    river_choice = input("Type T for (TORCH) or R for (ROPE): ").upper()
    return river_choice

def wrong_answer():
    # Wrong asnswer
    print("STOP TRYING TO BREAK THE GAME!")
    print("The Burj Khalifa teleports above you and crushes you. lel")

def torch_death():
    '''This is the players daeth when they walk to the torch'''
    print("You reach for tghe torch and feel a knife stab your back.")
    print("After that, the Burh Khalifa teleports above your head and crushes you")

def dragons_lair():
    '''This is the players choice of wehter to fight the dragon or not'''
    print("You see the dragon sleeping and a dark room off to the side.")
    river_choice = input("Please enter S for SLAY, or R for ROOM ").upper()
    return river_choice


def cls():
    print ('\n' * 60)

cls()

print("10010101100010" * 5)
print('''                                                                          
   (    (                    (     (                      )               
   )\   )\    (   (  (       )\    )\ )  )     (       ( /(  (  (     (   
 (((_|(((_)(  )\  )\ )\   ((((_)( (()/( /((   ))\ (    )\())))\ )(   ))\  
 )\___)\ _ )\((_)((_|(_)   )\ _ )\ ((_)|_))\ /((_))\ )(_))//((_|()\ /((_) 
((/ __(_)_\(_) \ / /| __|  (_)_\(_)_| |_)((_|_)) _(_/(| |_(_))( ((_|_))   
 | (__ / _ \  \ V / | _|    / _ \/ _` |\ V // -_) ' \))  _| || | '_/ -_)  
  \___/_/ \_\  \_/  |___|  /_/ \_\__,_| \_/ \___|_||_| \__|\_,_|_| \___|  
''')

print("10010101100010" * 5)

# 1st choice
print("You see a cave split into a left and right tunnel.")
print("<")
print("Do you choose to go left or right?")
print("<")
cave_choice = input("Enter R for right or L for left: ").upper()

if cave_choice == "L" or cave_choice == "LEFT":
    
    # Left cave
    
    river_choice = left_cave()
    
    if river_choice == "B" or river_choice == "BOAT":
        
        # Boat Choice
        
        print("You climb into the wooden boat and push off")
        
        # Death scene
        
        print("Everything is going smoothly, but then you realize that the wood from the boat is 0.000001 mm thick so it breaks and you get eaten by evil josh dun's")
        
    elif river_choice == "S" or river_choice == "SWIM":
        
        #Swim Choice
        
        print("You take a deep breath and dive into the cold river.")
        
        print("Everything is going swimmingly, (get it) but then you realize that you didn't take any swim lessons! You start to drown but then a magestic Cam Newton comes and saves you!")
        
        # Get the treasure
        
        print("You get the treasure and dab with him!")
        
    elif river_choice == "W" or river_choice == "WALK":
        
        print("You start walking along the narrow edge of the river.")
        
        # Death scene
        
        print("You can see the treasure! You get excited but then you trip on a rock and smash your face into the ground. You die from a fatal concussion.")
    else:
        # Wrong answer
        wrong_answer
        
elif cave_choice == "R" or cave_choice == "RIGHT":
    river_choice = right_cave()
    if river_choice == "T" or river_choice == "TORCH":
        print("You walk toards the torch and die for no reason. lel")
        # TODO: Add death function for TORCH
    elif river_choice == "R" or river_choice == "ROPE":
        print("You grab te rope and lower youself down the hole.")
        print("You hear a dragon breathing in the dark room.")
        # TODO add a dragon choice
        river_choice = dragons_lair()
        if river_choice == "S" or river_choice == "SLAY":
            print("DED")
        elif river_choice == "R" or river_choice == "ROOM":
            print("YOU WIN!")
else:
    # Wrong answer
    wrong_answer()

