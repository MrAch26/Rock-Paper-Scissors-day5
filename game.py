import random


class Game:
    Valids = ["rock", "paper", "scissors", "r", "p", "s"]

    def get_user_item(self, usr_name, usr_input=None):
        """
        gets user input for rsp
        :param usr_input: usr_input, NONE if User, if computer, Computer calls function with input
        :arg usr_name
        :return: returns user_input if valid
        """

        if usr_input is None:
            usr_input = input(f"{usr_name} enter Rock, Paper or Scissors?\n").lower()
            if usr_input not in self.Valids or usr_input.isnumeric():
                print(f"You didn't enter a valid choice, it has to be one of the below \n {self.Valids}")
                usr_input = self.get_user_item(usr_name)
        else:
            print(f"{usr_name} enter Rock, Paper or Scissors?\n")
        return usr_input

    def get_computer_item(self):
        """:return calls get_user_item and passes random choice from Valids"""
        valids = ['rock', 'paper', 'scissors']
        computer_input = random.choice(valids)
        self.get_user_item("Computer", computer_input)
        return computer_input

    @staticmethod
    def get_game_result(user_item, computer_item):
        """:return outcome [win, loss, draw]
        """
        outcome = "loss"
        if user_item == computer_item or user_item == "r" and computer_item == "rock" or user_item == "p" and computer_item == "paper" or user_item == "s" and computer_item == "scissors":
            outcome = "draw"
        else:
            if user_item == "rock" and computer_item == "scissors" or user_item == "r" and computer_item == "scissors" or user_item == "rocks" and computer_item == "scissors":
                outcome = "win"
            elif user_item == "paper" and computer_item == "rock" or user_item == "p" and computer_item == "rock" or user_item == "papers" and computer_item == "rock":
                outcome = "win"
            elif user_item == "scissors" and computer_item == "paper" or user_item == "s" and computer_item == "paper" or user_item == "scissors" and computer_item == "paper":
                outcome = "win"
        return outcome.lower()

    def play(self):
        """
        Plays the game with computer opponent. prints and returns outcome
        :return returns outcome of the round
        """
        you = self.get_user_item("Player 1")
        computer = self.get_computer_item()
        results_game = self.get_game_result(you, computer)
        print(f"You chose {you}, the computer chose {computer}! You scored a {results_game.upper()}")
        return results_game


def main():
    game1 = Game()
    game1.play()


if __name__ == '__main__':
    main()
