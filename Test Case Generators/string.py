import random

#generate a random string comprised of 0's and 1's with a length between 30 and 50 characters
def generate_random_string():
    length = random.randint(30, 50)
    return ''.join(random.choices(['0', '1'], k=length))

#print(generate_random_string())

import string

def generate_password(length):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
    return ''.join(random.choice(letters) for i in range(length))

"""for i in range(10):
    print('"'+generate_password(8)+'"')"""