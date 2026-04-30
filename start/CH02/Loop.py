"""""
Create a loop conditional that takes an imput and if it's a yes then print it 10 times when return a reply
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