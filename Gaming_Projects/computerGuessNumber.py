"""
Computer guesses the secret number entered by the user
Author : Monisha Sivaraj
Date : 15/01/2021
"""

import random
def computer_guess(endValue):
    leastvalue = 1
    highestvalue = endValue
    feedback = ''
    while feedback != 'c' :
        if leastvalue != highestvalue:
            guess_value = random.randint(leastvalue, highestvalue)
        else:
            guess_value = leastvalue  # could also be highestvalue
        feedback = input(f'Is {guess_value} too high (H) ,too low (L) or correct (C) ??')
        if feedback == 'h' :
            highestvalue = guess_value - 1
        elif feedback == 'l' :
            leastvalue = guess_value + 1

    print(f'Yay! The computer guessed the number, {guess_value} correctly!!!')


computer_guess(100)  # can change the value range
