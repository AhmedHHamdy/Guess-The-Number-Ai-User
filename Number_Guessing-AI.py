import random

def ai_guessing():
    #random number from the range
    ai_guess = random.choice(range(1, 10))
    return ai_guess


def user_guessing():
    number_tries = 0
    guess = ai_guessing()
    while True:
        #we are trying if the user_guess_1 had provide an int if it wasn't an int e pass 'Invalid Value'
        try:
            if number_tries < 6:
                user_guess = int(input("Guess a number between 1-10: "))
                number_tries += 1
                if guess == user_guess:
                    print('Congratulation! You Won!')
                    break
                else:
                    print('Try again')
                    continue
            print('You lost, you passed the number of tries')
            break
        except:
            print("Wrong Input!!! Try Again")
            continue

if __name__ == "__main__":
    user_guessing()

    