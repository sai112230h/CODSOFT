import random
import string

# Function to generate password
def generate_password(length):
    # Character set includes letters, digits, and special symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters to form the password
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

# Main program starts here
print("----- Password Generator -----")

# Taking input from user
length = int(input("Enter the desired password length: "))

# Checking if length is valid
if length > 0:
    # Calling function to generate password
    result = generate_password(length)
    print("Your Generated Password is:", result)
else:
    print("Invalid length! Please enter a number greater than 0.")