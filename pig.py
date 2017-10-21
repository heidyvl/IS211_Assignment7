import random
import sys

def number_of_players(message):
    while True:
        try:
            number = int(input(message))
        except(SyntaxError, ValueError):
            continue
                
        return number


class RolledOneException(Exception):
    pass


class Dice:

    def __init__(self):
        self.value = random.randint(1, 6)

    def roll(self):

        self.value = random.randint(1, 6)
        if self.value == 1:
            raise RolledOneException

        return self.value


    def __str__(self):
        return "Rolled " + str(self.value) + "."


class ScoreHolder:

    def __init__(self):
        self.value = 0


    def reset_score(self):
        self.value = 0


    def add_dice_value(self, dice_value):
        self.value += dice_value


class Player(object):

    def __init__(self, name=None):
        self.name = name
        self.score = 0


    def add_score(self, player_score):
        self.score += player_score

    def action(self, promt, zero, one):
        action = None
        while action != 0 or action != 1:
            try:
                action = int(input(" Enter '1' to Roll, or '0' to Hold? "))
            except:

                SyntaxError, ValueError
           
            return action

    def __str__(self):
        return str(self.name) + ": " + str(self.score)

class ComputerPlayer(Player):
    cpu_names=[]

    def __init__(self, number):
        name = 'Compu {}'.format(number)

        super(ComputerPlayer, self).__init__(name)


    def keep_rolling(self, score_holder):
        while score_holder.value < (25 or 100-score_holder.value):
            print('  {} will roll again.'.format(self.name))
            return True
        print('  {} will hold.'.format(self.name))
        return False


class HumanPlayer(Player):
    def __init__(self, name):
        super(HumanPlayer, self).__init__(name)


    def keep_rolling(self, score_holder):
        human_decision = None
        while human_decision != 0 or human_decision != 1:
            try:
                human_decision = Player().action(" Enter '1' to Roll, or '0' to Hold? ", 0, 1)
                if human_decision == 1:
                    return True
                if human_decision == 0:
                    return False
            except:
                SyntaxError, ValueError
                
class Game:
    def __init__(self,player1,player2):
        self.players = []
        self.human = HumanPlayer(Player)
        self.compu = ComputerPlayer(Player)
        self.score_holder = ScoreHolder()
        self.dice = Dice()
        for i in range(player1):
            player_name = raw_input('Enter name of player number. {}: '.format(i+1))
            if player_name == '':
                player_name = 'Player {}'.format(i+1)
            self.players.append(HumanPlayer(player_name))
        for i in range(player2):
            self.players.append(ComputerPlayer(i+1))
        self.number_of_players = len(self.players)
    def objective(self):

        print("*" * 70)
        print("Welcome to Pig Dice!" .center(70))
        print("*" * 70)
        print('The game of Pig is a very simple jeopardy dice game in which two players'.center(70))
        print('race to reach 100 points'.center(70))
        print('Each turn, a player repeatedly rolls a die until either a 1 is rolled'.center(70))
        print('or the player holds and scores the sum of the rolls (i.e. the turn total'.center(70))
        print('At any time during a players turn, the player is faced with two decisions: .'.center(70))
        print('roll - If the player rolls a: ')
        print('        1: the player scores nothing and it becomes the opponents turn.')
        print('        2-6: the number is added to the players turn total and the turn continues.')
        print('hold - The turn total is added to the players score and it becomes the opponents turn.')

        

    def decide_first_player(self):
        self.current_player = random.randint(1, self.number_of_players) % self.number_of_players
        print('{} starts'.format(self.players[self.current_player].name))


    def next_player(self):
        self.current_player = (self.current_player + 1) % self.number_of_players



    def previous_player(self):
        self.current_player = (self.current_player - 1) % self.number_of_players


    def get_all_scores(self):
        return ', '.join(str(player) for player in self.players)


    def play_game(self):
        self.objective()
        self.decide_first_player()
        while all(player.score < 100 for player in self.players):
            print('\nCurrent score --> {}'.format(self.get_all_scores()))
            print('\n*** {} is your turn '.format(self.players[self.current_player].name))
            self.score_holder.reset_score()

            while self.keep_rolling():
                pass

            self.players[self.current_player].add_score(self.score_holder.value)
            self.next_player()

        self.previous_player()
        print(' {} you are the winner!!!!!!! '.format(self.players[self.current_player].name).center(70, '*'))
        action = None
        while action != 0 or action !=1:
            try:
                action = input('Press 1 to play again or 0 to quit ')
                if action == 1:
                    self.score_holder.reset_score()
                    main()
                else:
                    sys.exit()
            except (ValueError, SyntaxError):
                continue


    def keep_rolling(self):
        try:
            dice_value = self.dice.roll()
            self.score_holder.add_dice_value(dice_value)
            print('Last roll: {}, new score holder value: {}'.format(dice_value, self.score_holder.value))
            return self.players[self.current_player].keep_rolling(self.score_holder)

        except RolledOneException:
            print('  Rolled one. Switching turns')
            self.score_holder.reset_score()
            return False
def main():

    print "Welcome to Pig"
    human = None
    compu = None
    while human <= 0 and compu <=0:
        human = number_of_players('How many humans are playing today? ')
        compu = number_of_players('How many computers are playing today? ')
    game = Game(human, compu)

    game.play_game()

if __name__ == '__main__':
    main()
  
            
