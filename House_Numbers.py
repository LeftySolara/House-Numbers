# To do:
#   - output multiple winners in case of tie
#   - write method to play a specific number of rounds
#   - linke to text file containing rules
#   - write more unit tests for weird input

from die import Die

class Player(object):
    """Represents one player"""
    def __init__(self, name):
        self.name = name
        self.scores = []
        self.wins = 0

    def __str__(self):
        return self.name

    def last_score(self):
        return self.scores[-1]

    def total_score(self):
        return sum(self.scores)

    def get_wins(self):
        return self.wins


class HouseNumbers(object):
    """Represents a game of House Numbers. Keeps track of players,
    scores, wins, etc."""

    def __init__(self, player_names = ["Player 1"]):
        self.players = [Player(name) for name in player_names]
        self.die = Die()
        self.round = 1  # current (uncompleted) round

    def __str__(self):
        for player in self.players:
            print(player)

    def print_round(self, winner):
        """Displays summary of the given round"""
        print("Round {}:".format(self.round))
        for player in self.players:
            print("{}: {}".format(player.name, player.scores[self.round-1]))

        print("\nWinner: {}".format(winner.name))

    def play_round(self):
        """Simulates one round of House Numbers"""
        winner = self.players[0]

        for player in self.players:
            print("It's {}'s turn!".format(player.name))
            rolls = ['0','0','0']
            score = "".join(rolls)
            for i in range(3):
                print("Current score: {}".format(score))
                print("rolling...")
                roll = self.die.roll()
                print("You rolled a {}!".format(roll))
                choice = ""
                valid = False

                while not valid:
                    if not choice.isdigit():
                        pass
                    elif choice.isdigit() and int(choice) not in range(1,4):
                        print("Invalid position. Try again.")
                    elif int(choice) in range(1,4) and rolls[int(choice)-1] != '0':
                        print("Position already used. Try again")
                    elif int(choice) in range(1,4) and rolls[int(choice)-1] == '0':
                        valid = True
                        break
                    choice = input("Put roll in what position? ")
 
                if choice == "1":
                    rolls[0] = roll
                elif choice == "2":
                    rolls[1] = roll
                elif choice == "3":
                    rolls[2] = roll

                score = "".join(str(i) for i in rolls)

            player.scores.append(int(score))
            if int(score) > winner.last_score():
                winner = player
        
            print("{} : {}".format(player, score))
            print()
        
        winner.wins += 1
        self.print_round(winner)