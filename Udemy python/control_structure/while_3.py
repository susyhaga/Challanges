# Stop when the random number is discovered in the input
from random import randint

input_number = -1
secret_number = randint (0,10)

while input_number != secret_number:
    input_number = int(input("Guess the random number:"))
print("The secret number {} was found!" .format(secret_number))

