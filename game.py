# import rps
import random

class Game:

    def get_user_item(self, usr_name, usr_input=None):
        """
        gets user input for rsp
        :arg usr_name, usr_input, NONE if User, if computer, Computer calls function with input
        :return: returns user_input if valid
        """
        valids = ["rock", "paper", "scissors"]
        if usr_input is None:
            usr_input = str(input(f"{usr_name} enter Rock, Paper or Scissors?\n")).lower()
            if usr_input not in valids and usr_input.isalpha():
                print(f"You didn't enter a valid choice, it has to be one of the below \n {valids}")
                self.get_user_item(usr_name)
        else:
            print(f"{usr_name} enter Rock, Paper or Scissors?\n")
        return usr_input

    def get_computer_item(self):
        """:return calls get_user_item and passes random choice from valids"""
        valids = ["rock", "paper", "scissors"]
        computer_input = random.choice(valids)
        self.get_user_item("Computer", computer_input)
        return computer_input



def main():
    game1 = Game()
    game1.get_user_item("Player 1")
    print(game1.get_computer_item())


if __name__ == '__main__':
    main()
