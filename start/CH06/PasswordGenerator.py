'''
Password generator

This is a secure password generator that generates a password with a minimum length of 8
'''
#libraries used
import random
import string


#Define character pools
UPPERCASE  = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SPECIAL = r"!@#$%^&*()_-:<>"

#Minimum password length 
MIN_LENGTH = 8

#helper function 

def get_yes_or_no(prompt: str) -> bool:
    '''Ask the user for a yes or no question'''
    while True: 
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter yes / no: ")

def get_password_length() -> int:
    while True:
        try:
            length = int(input("How long do you want password?"))
            if length >= MIN_LENGTH:
                return length
            print("please enter a valid length, try again ")
        except ValueError:
            print("please enter a whole number")
    
def get_criteria() -> dict:
    '''Take length, uppercase, lowercase, digits, special char input from user'''
    length = get_password_length()

    criteria = {
        "length": length, 
        "uppercase": get_yes_or_no(" Do you want uppercase letters?"),
        "lowercase": get_yes_or_no(" Do you want lowercase letters?"),
        "digits": get_yes_or_no(" Do you want numbers/digits?"),
        "special": get_yes_or_no(" Do you want special characters?"),
    }

    #Validator of criteria
    if not any([criteria ["uppercase"], criteria["lowercase"],
            criteria["digits"], criteria["special"]]):
        print(" You must select at least one character type, try again")
        return get_criteria()
    return criteria

def build_pool(criteria: dict) -> tuple[str, list[str]]:
    '''this is a character pool'''
    pool = ""
    required = []

    if criteria["uppercase"]:
        pool += UPPERCASE
        required.append(random.choice(UPPERCASE))

    if criteria["lowercase"]:
        pool += LOWERCASE
        required.append(random.choice(LOWERCASE))

    if criteria["digits"]:
        pool += DIGITS
        required.append(random.choice(DIGITS))

    if criteria["special"]:
        pool += SPECIAL
        required.append(random.choice(SPECIAL))
    return pool, required

def generate_password(criteria: dict) -> str:
    ''' Generation of password creator'''
    pool, required = build_pool(criteria)
    length = criteria["length"]

    #Fill any remaining spots with random characters
    remaining_count = length = len(required)
    remaining = [random.choice(pool) for _ in range (remaining_count)]

    password_chars = required + remaining
    random.shuffle(password_chars)


    return "". join(password_chars)


def main():

    while True:
        criteria = get_criteria()
        password = generate_password(criteria)
        print("This is your generated password: ")
        print(f"{password}")

        if not get_yes_or_no("Generated another password? (y/n): "):
            print("Stay Secure")
            break
        print()

if __name__ == "__main__":
    main()