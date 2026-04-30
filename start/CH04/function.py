'''
Create a conditional that takes an input and if its a year then return a reply
'''

#This is going to take an input from the user
answer = input("is today a good day? (y/n) ").lower()

'''
Loops Yea it is if the response is equal to yes
'''
def send_message():
     for x in range (10):
          print("Yeah it is!")
        
#Its an if statement checking if the string is equal to y and if so print yes it is
if answer == "y":
        send_message()
elif answer == "n":
    print("Im sorry")
else:
    print("Please try again")