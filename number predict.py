# This is a Number guessing program
# First import random  
import random
# In here showing title
print (" \t NUMBER GUESSING GAME")
print ("\n")
# Ask user to type their name 
name = input (" Enter your name : ")
print ("\n")
# Giving positive greeting for the user
print ("\t Let's play the Game", name.upper(),"..... " \
       "GOOD LUCK !!!")
print ("\n")

num = random.randint(1,100)

num1 = num + 235
num2 = num * 30
print ("__ + 235 = ",num1)
print ("\n")
print ("__ * 30 = ",num2)
print ("\n")
turns = 5
while turns > 0:
    number = int(input("Enter you Guess Number : ")) 
    turns -= 1
    if number == num :
        print ("\n")
        print ("\t CONGRATS",name, "YOU WON THE GAME" )
        print ("\n")
        print ( "\t THE NUMBER IS ",num)
        break

    if number != num :
        print ("\n")
        print (" \t THIS IS WRONG NUMBER, TRY AGAIN")
        print ("\n")
        print (" Only left ",turns, "turns")
        print ("\n")

    if turns == 0:
        print ("\n")
        print (" Oh noo...!!! You loose....sorry ")
        print ("\n")

        
                  


 