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
# This function will Choose one number in between 1 and 100
num = random.randint(1,100)
# Give some hints to guess the number
# Here I give two hints
# One is Addition and second one is multiplication 
  
num1 = num + 235
num2 = num * 30
print ("__ + 235 = ",num1)
print ("\n")
print ("__ * 30 = ",num2)
print ("\n")
# Now give turns for guess
turns = 5
# Create the while loop,The code will work till the turns goes to zero
while turns > 0:
    number = int(input("Enter you Guess Number : ")) 
# Every time user enter a number then turns will reduse one by one 
    turns -= 1
# In "if condition" check user enter the currect number or not 
# If the guess number is correct 
# Then the 'if function' will Break   
    if number == num :
        print ("\n")
        print ("\t CONGRATS",name, "YOU WON THE GAME" )
        print ("\n")
        print ( "\t THE NUMBER IS ",num)
        break
# If entered number was wrong
# That will show 
# And also shows the remaing turns 
    if number != num :
        print ("\n")
        print (" \t THIS IS WRONG NUMBER, TRY AGAIN")
        print ("\n")
        print (" Only left ",turns, "turns")
        print ("\n")
# When turns became zero game will end with the messaege
    if turns == 0:
        print ("\n")
        print (" Oh noo...!!! You loose....sorry ")
        print ("\n")

        
                  


 