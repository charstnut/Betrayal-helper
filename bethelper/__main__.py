"""
This file is the main script for the helper module
"""


class Game:
    ### Game class
    def __init__(self, num_players: int):
        if num_players < 3 or num_players > 5:
            raise ValueError("Number of players can only be 3 to 5.")
        self._num_player = num_players
        self._families = []  # A list of families/players in this game

    def init_game(self):
        """
        Initialize the game
        """
        pass

    def status(self):
        """
        Print the status of the game
        """
        self.print_families()
        self.print_map()
        print("Currently it's {}'s turn.".format(self.current_player()))

    def print_families(self):
        """
        Print all the families in order and list their attributes
        """
        for f in self._families:
            print("Family member: {}".format(f.name))


if __name__ == '__main__':
    game = Game(num_players=3)
