# Gives the name of the game
print ("\t FLAMES")
print ("\n")
# Take input from user
# And Saved them in lowercase
name1 = input("Name of the first person : ").lower()
name2 = input("Name of the second person : ").lower()
print ("\n")
# If there any space in between names
# In this stage removing all the spaces
rename1 = name1.replace(" ", "")
rename2 = name2.replace(" ", "")
name = rename1 + rename2
for x in name:
        if name.count(x) != 1:
            name = name.replace(x,"")
            print (name)