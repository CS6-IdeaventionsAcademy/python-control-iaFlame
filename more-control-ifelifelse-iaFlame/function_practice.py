# Tristan Kang
# Dec 12th, 2017
# Function Practice


# Mr. Allan

import math


# Chez

def cheese():
    '''Makes a screen full of I like cheeses!'''
    print ("I like cheese!" * 200)

cheese()


# Volume of Sphere

def volume_sphere(radius):
    '''Calculates the volume of a sphere radius is an integer oor float'''
    volume = (4/3)*math.pi*r**3
    print("Calculating.")
    print("Calculating..")
    print("Calculating...")
    print("Calculating.")
    print("Calculating..")
    print("Calculating...")
    return volume

r = input("Please enter a radius of a sphere: ")
r = float(r)
v_sphere = volume_sphere(r)
print(v_sphere)


# Fahrenheit to Celsius

def temp_C(temp_F):
    '''Converts a temperature in Fahrenheit to Celsius temp_F is the
temperature (float) in Fahrenheit'''
    #(T(F) - 32) x 5/9
    answer = (temp_F - 32) * (5/9)
    return answer

    t_in_F = input("Please enter a temperature in Fahrenheit: ")
    t_in_F = float(t_in_F) #Converting the input to a float "52.0 --> 52.0
    t_in_C = temp_C(t_in_F)
    print("That temperature in Celsius is",t_in_C)


# Cam Newton Touchdowns

def cam_newton_TDS(TDS):
    cam_newton_TDS = TDS * 7*4*math.pi+6
    return cam_newton_TDS
TDS_guess = input("Enter how many TDS you think Cam Newton has: ")
TDS_guess = float(TDS_guess)
print("WRONG! He has:")
print(cam_newton_TDS(TDS_guess))
print("TDS")
