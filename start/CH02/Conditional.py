"""""
Create a conditional that takes an imput and if it's a yes then return a reply
"""

#This is going to take an input from the user
answer = input("Is today a good day? (y/n) ").lower()


#This is an if statement checking if the string is equal to y and if so print yes it is
if answer == "y":
    print("Yes it is")
elif answer == "n":
    print("Im sorry")
else:
    print("Please try again")