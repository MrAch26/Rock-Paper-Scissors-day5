class RPS:
    # def __init__(self):
    # results_win = the end return of game.py
    Results = {'Win': 0, 'Loss': 0, 'Draw': 0}

    def print_results(self):

        if self.results_game == 'win':
            self.Results["Win"] += 1
            print(self.Results)
        elif self.results_game == 'loss':
            self.Results["Loss"] += 1
            print(self.Results)
        elif self.results_game == 'draw':
            self.Results["Draw"] += 1
            print(self.Results)
    def Play_again(self):
        play_again = str(input("Do you want to play again ? y or n")).lower()
        while play_again != 'y' and play_again != 'n':
            play_again = str(input("It must be 'y' or 'n' ")).lower()
        else:
            if play_again == 'y':
                print("Let's Play again!")
                self.results_game = input('win loss draw')
                self.Play_again()


            elif play_again == 'n':
                print("back to the menu...")
                self.get_user_menu_choice()

    def get_user_menu_choice(self):
        users_choice = str(input("Do you want to play (p)\nOr show results (s)\nOr exit the game (e) ?")).lower()
        while users_choice != 'p' and users_choice != 's' and users_choice != 'e':
            users_choice = str(input("It must be 'p' or 's' or 'e' "))
            # print("Menu:\n")
        else:
            if users_choice == 'p':
                print("Lets play !")
                self.results_game = input('win loss draw')
                self.Play_again()

            elif users_choice == 's':
                print('Here are your results')
                self.print_results()
                self.get_user_menu_choice()

            elif users_choice == 'e':
                exit()





def main():
    print("Welcome to the Rock Paper Scissors Game !")
    print('\t--Menu--')
    game = RPS()
    game.get_user_menu_choice()


if __name__ == '__main__':
    main()
