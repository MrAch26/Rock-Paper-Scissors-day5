class RPS:
    def __init__(self):
        self.results_game = int(input("type number 012"))
    # results_win = the end return of game.py

    def print_results(self):
        results={'Win':0,'Loss':0,'Draw':0 }
        if self.results_game == 0:
            results["Win"] += 1
        elif self.results_game == 1:
            results["Loss"] += 1
        elif self.results_game == 2:
            results["Draw"] += 1


    def get_user_menu_choice(self):
        users_choice = str(input("Do you want to play or show results ? (p or s)"))
        while users_choice != 'p' and users_choice != 's':
            users_choice = str(input("It must be 'p' or 's' "))
            # print("Menu:\n")
        else:
            if users_choice == 'p':
                print('Lets play !')
                self.results_game

            elif users_choice == 's':
                print('Here are your results')
                self.print_results()





def main():
    print('Menu:')
    r = RPS()
    r.get_user_menu_choice()


if __name__ == '__main__':
    main()
