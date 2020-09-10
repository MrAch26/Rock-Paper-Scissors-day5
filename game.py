# import rps
import random


class Game:

    def get_user_item(self, usr_name, usr_input=None):
        """
        gets user input for rsp
        :param usr_input: usr_input, NONE if User, if computer, Computer calls function with input
        :arg usr_name
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

    @staticmethod
    def get_game_result(user_item, computer_item):
        """:return outcome [win, loss, draw]
        """
        outcome = "loss"
        if user_item == computer_item:
            outcome = "draw"
        else:
            if user_item == "rock" and computer_item == "scissors":
                outcome = "win"
            elif user_item == "paper" and computer_item == "rock":
                outcome = "win"
            elif user_item == "scissors" and computer_item == "paper":
                outcome = "win"
        return outcome

    def play(self):
        """
        Plays the game with computer opponent. prints and returns outcome
        :return returns outcome of the round
        """
        you = self.get_user_item("Player 1")
        computer = self.get_computer_item()
        outcome = self.get_game_result(you, computer)
        print(f"You chose {you}, the computer chose {computer}! You scored a {outcome.upper()}")
        return outcome


def main():
    game1 = Game()
    game1.play()


if __name__ == '__main__':
    main()
