import time
import itertools
import string


def bruteforce(real):
    startTime = time.perf_counter()
    # Define the character set
    chars = string.ascii_letters + string.digits + string.punctuation

    attempts = 0
    for password_length in range(1, 9):  # Adjust the password length range as needed
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            print(guess + "\n")
            if guess == real:
                endTime = time.perf_counter()
                return 'Password found: {}. Found in {} guesses, took {} seconds'.format(guess, attempts,endTime-startTime)

#input your target password here
target_password = 'pwd'
print(bruteforce(target_password))
