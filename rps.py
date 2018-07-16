import random

class Player():
  valid_moves = ['rock', 'papper', 'scissor']

  def play(self):
    return Player.valid_moves[0]

class RandomPlayer(Player):
  def play(self):
    index = random.randint(0,2)
    return Player.valid_moves[index]


class HumanPlayer(Player):
  def play(self):
    player_move = input('Enter your move (rock, papper or scissor):\n')
    while player_move not in Player.valid_moves:
      player_move = input('Invalid move, try again')
    return player_move

class Game():

  def start(self):
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    game_result = 0
    while game_result == 0:
      player1_move = player1.play()
      player2_move = player2.play()
      game_result = self.check_result(player1_move, player2_move)
      if game_result == 0:
        print('Draw!\n')
    print('Player ' + str(game_result) + ' won!\n')
  
  def check_result(self, move1, move2):
    print('Player 1 choose "' + move1 + '" and player 2 choose "' + move2 + '"')
    if self.is_move_stronger(move1, move2):
      return 1
    elif self.is_move_stronger(move2, move1):
      return 2
    else:
      return 0

  def is_move_stronger(self, move1, move2):
    if (move1 == 'rock' and move2 == 'scissor'):
      return True
    elif (move1 == 'scissor' and move2 == 'papper'):
      return True
    elif (move1 == 'papper' and move2 == 'rock'):
      return True
    return False

game = Game()
game.start()