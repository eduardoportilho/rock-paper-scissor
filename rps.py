import random

valid_moves = ['rock', 'papper', 'scissor']

class Player():
  def __init__(self):
    self.score = 0

  def play(self):
    return valid_moves[0]

class RandomPlayer(Player):
  def play(self):
    index = random.randint(0,2)
    return valid_moves[index]


class HumanPlayer(Player):
  def play(self):
    player_move = input('Enter your move (rock, papper or scissor):\n')
    while player_move not in valid_moves:
      player_move = input('Invalid move, try again')
    return player_move


class Game():
  def __init__(self):
    self.player1 = RandomPlayer()
    self.player2 = RandomPlayer()

  def start(self):
    input('Let\'s play Rock, Papper or Scissors!\nPress enter to play\n')
    try:
      while True:
        self.play_round()
        print('The score is: ' + str(self.player1.score) + ' x ' + str(self.player2.score) + '\n')
        input('Press enter to play again or ctrl+C to quit\n')
    except KeyboardInterrupt:
      print('\nThanks for playing!')
  

  def play_round(self):
      player1_move = self.player1.play()
      player2_move = self.player2.play()
      result = Game.check_result(player1_move, player2_move)
      print('Player 1 choose "' + player1_move + '" and player 2 choose "' + player2_move + '"')
      if result == 1:
        self.player1.score += 1
        print('=> Player 1 won!\n')
      elif result == 2:
        self.player2.score += 1
        print('=> Player 2 won!\n')
      else:
        print('=> Draw!\n')

  @classmethod
  def check_result(cls, move1, move2):
    if Game.is_move_stronger(move1, move2):
      return 1
    elif Game.is_move_stronger(move2, move1):
      return 2
    else:
      return 0

  @classmethod
  def is_move_stronger(cls, move1, move2):
    if (move1 == 'rock' and move2 == 'scissor'):
      return True
    elif (move1 == 'scissor' and move2 == 'papper'):
      return True
    elif (move1 == 'papper' and move2 == 'rock'):
      return True
    return False

game = Game()
game.start()