import random
import getpass

def user_guessing():
    number_tries = 0
    while True:
        try: 
            #We are using getpass to hide the input from the user but you can use input function if you want
            user_guess_2 = int(getpass.getpass("input a number from 1-10:> "))
            while True:
                #we are trying if the user_guess_1 had provide an int if it wasn't an int e pass 'Invalid Value'
                try:
                    if number_tries < 6:
                        user_guess_1 = int(input("Guess a number between 1-10: "))
                        number_tries += 1
                        if user_guess_2 == user_guess_1:
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
        except:
            print("Invalid Value, Try Again")
            continue

        break
            
    

if __name__ == "__main__":
    user_guessing()
