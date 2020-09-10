from game import *


class RPS:
    Results = {'Win': 0, 'Loss': 0, 'Draw': 0}
    # results_print = print(f"Win : {Results['Win']}")
    results_game = ''

    def update_results(self):
        if self.results_game == 'win':
            self.Results["Win"] += 1
        elif self.results_game == 'loss':
            self.Results["Loss"] += 1
        elif self.results_game == 'draw':
            self.Results["Draw"] += 1

    def print_results(self):
        if self.results_game == 'win':
            print(f"Win: {self.Results['Win']}\nLoss: {self.Results['Loss']}\nDraw: {self.Results['Draw']}\n " )
        elif self.results_game == 'loss':
            print(f"Win: {self.Results['Win']}\nLoss: {self.Results['Loss']}\nDraw: {self.Results['Draw']}\n " )
        elif self.results_game == 'draw':
            print(f"Win: {self.Results['Win']}\nLoss: {self.Results['Loss']}\nDraw: {self.Results['Draw']}\n " )

    def Play_again(self):
        play_again = (input("Do you want to play again ? y or n")).lower()
        while play_again != 'y' and play_again != 'n':
            play_again = (input("It must be 'y' or 'n' ")).lower()
        else:
            if play_again == 'y':
                print("Let's Play again!")
                game1 = Game()
                self.results_game = game1.play()
                self.update_results()
                self.Play_again()


            elif play_again == 'n':
                print("back to the menu...")
                self.get_user_menu_choice()

    def get_user_menu_choice(self):
        users_choice = (input("Do you want to play (p)\nOr show results (s)\nOr exit the game (e) ?")).lower()
        while users_choice != 'p' and users_choice != 's' and users_choice != 'e':
            users_choice = (input("It must be 'p' or 's' or 'e' ")).lower()
            # print("Menu:\n")
        else:
            if users_choice == 'p':
                print("Lets play !")
                game1 = Game()
                self.results_game = game1.play()
                self.update_results()
                self.Play_again()

            elif users_choice == 's':
                if self.Results['Win'] == 0 and self.Results['Loss'] == 0 and self.Results['Draw'] == 0:
                    print("You didn't Play yet !\n")
                    self.print_results()
                    self.get_user_menu_choice()

                else:
                    print('\npHere are your results:')
                    self.print_results()
                    self.get_user_menu_choice()



            elif users_choice == 'e':
                print("Good Bye ! Thank you 👨🏿‍💻")
                exit()


def main():
    print("Welcome to the Rock Paper Scissors Game !")
    print('\t--Menu--')
    game = RPS()
    game.get_user_menu_choice()


if __name__ == '__main__':
    main()
