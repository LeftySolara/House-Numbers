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

    def add_win(self):
        self.wins += 1

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

    def print_round(self, winners):
        """Displays summary of the given round"""
        print("Round {}:".format(self.round))
        for player in self.players:
            print("{}: {}".format(player.name, player.scores[self.round-1]))

        for player in winners:
            print("Winner: {}".format(player))

    def play_round(self):
        """Simulates one round of House Numbers

        Each player rolls a die three times. On each roll, the player chooses
        what digit of their score the roll will represent (ones, tens, hundreds).
        """

        winners = []
        round_scores = {}

        for player in self.players:
            print("It's {}'s turn!".format(player.name))
            rolls = ['0','0','0']
            score = "".join(rolls)
            for i in range(3):
                print("\nCurrent score: {}".format(score))
                print("rolling...")
                roll = self.die.roll()
                print("You rolled a {}!".format(roll))
                choice = ""
                valid_choice = False

                while not valid_choice:
                    if not choice.isdigit():
                        pass
                    elif choice.isdigit() and int(choice) not in range(1,4):
                        print("Invalid position. Try again.")
                    elif int(choice) in range(1,4) and rolls[int(choice)-1] != '0':
                        print("Position already used. Try again.")
                    elif int(choice) in range(1,4) and rolls[int(choice)-1] == '0':
                        valid_choice = True
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
            round_scores[player.name] = int(score)
        
            print("{} : {}".format(player, score))
            print()
        
        high_score = max(round_scores.values())
        for name in round_scores:
            if round_scores[name] == high_score:
                winners.append(name)

        for player in self.players:
            if player.name in winners:
                player.add_win()
        self.print_round(winners)

    def summary(self):
        """Displays stats of the game"""
        print("Total scores:")
        for player in self.players:
            print("{}: {}".format(player.name, player.total_score()))

        print("\nWins:")
        for player in self.players:
            print("{}: {}".format(player.name, player.get_wins()))