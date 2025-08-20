from easy import number_guessing_game_easy
from hard import number_guessing_game_hard
from medium import number_guessing_game_medium


def number_guessing_game():
            while True:  
                print("\nWelcome to the Number Guessing Game!")
                user3 = input("\nEnter 'q' to quit or 'p' to play\n")
                if user3 == 'q':   
                  break
                elif user3 == 'p':
                      print("Select level")
                      print("\n'e' for easy")
                      print("\n'm' for medium")
                      print("\n'd' for difficult\n")

                      user_level = input("")

                      if user_level == 'e':
                           number_guessing_game_easy()

                      elif user_level == 'm':
                           number_guessing_game_medium()
                    
                      elif user_level == 'd':
                            number_guessing_game_hard()
                     
                      else:
                            continue
                      

number_guessing_game()
