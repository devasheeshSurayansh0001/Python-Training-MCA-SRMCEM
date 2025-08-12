
'''
Number Guessing Game
Create a loop that keeps asking the user to guess a secret number until they get it right.
Guess the number: 5  
Wrong, try again.  
Guess the number: 8  
Correct! You guessed it.
'''
secret_number = 8  # The number to guess

while True:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong, try again.")