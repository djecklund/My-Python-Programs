
# Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1.
def findingCollatzConjecture():
    user_input = int(input("Enter a number: "))
    step = 0
    print('Your starting number is: ', user_input)
    while user_input != 1:
        if user_input % 2 == 0:
            user_input = user_input / 2
            step = step + 1
            print('Step ', step, ': ', user_input)
        else:
            user_input = user_input * 3 + 1
            step = step + 1
            print('Step ', step, ': ', user_input)

findingCollatzConjecture()
