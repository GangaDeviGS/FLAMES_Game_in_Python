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
# Added those name 
name = rename1 + rename2
# In here removing same characters
for x in name:
        if name.count(x) != 1:
            name = name.replace(x,"")
# Check total number of remaining characters            
number = len(name)
# List of FLAMES acronym

result = ["Friends","Love","Affection","Marriage","Enemy","Siblings"]   

# keep looping until only one item
# Is not remaining in the result list

while number > 1 :

# store that index value from
# where we have to perform slicing.
    split_result = (number % len(result) -1)
# this steps is done for performing
# anticlock-wise circular fashion counting.
    if split_result >= 0 :
          
          # list slicing
          right = result[split_result + 1:]
          left = result[: split_result]
          # list concatenation
          result = right + left
    else:
         result = result[: len(result) - 1]

# print final result     
print("Relationship status :", result[0])


       