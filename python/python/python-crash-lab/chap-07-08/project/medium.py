import random
import sys



def number_guessing_game_medium():
                count = 0
                
                while True:
                    computer_choice = random.randint(0, 50)
                    print("\nI have picked a number between 0 and 50.")
                    print("\nCan you guess what it is?")
                    
                
                    user = int(input("Enter your guess: "))
                    
                    if user > computer_choice:
                        count += 1
                        print("Too High! Try again.")
                        
                        
                    
                    elif user <  computer_choice:
                        count += 1
                        print("Too low! Try again.")
                        

                    elif user == computer_choice:
                        count += 1
                        print(f"Congratulation! You guessed it in {count} tries!")
                        print("Do you want to play again!")
                        user2 = input()
                        if user2 == 'p':
                            number_guessing_game_medium_1()
                        elif user2 == 'q':
                            sys.exit()
                            

def number_guessing_game_medium_1():
        
        count = 0
        while True:
            computer_choice = random.randint(0, 50)
            print("\nI have picked a new number between 0 and 50.")
            print("\nCan you guess what it is?")
            

            user = int(input("Enter your guess: "))
            
            if user > computer_choice:
                count += 1
                print("Too High! Try again.")
                
                
            
            elif user <  computer_choice:
                count += 1
                print("Too low! Try again.")
                

            elif user == computer_choice:
                count += 1

                print(f"Congratulation! You guessed it in {count} tries!")
                user2 = input("Do you want to play again\n")
                if user2 == 'p':
                    return number_guessing_game_medium_1()
                elif user2 == 'q':
                    sys.exit()
                        



