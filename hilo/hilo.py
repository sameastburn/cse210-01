import random

# verifies user input
class InputValidator:
  # ensures the user either inputs h or l
  def get(self):
    ready = False
    user_input = ''
    
    while (not ready):
      user_input = input('Higher or lower? [h/1] ')

      if user_input == 'h' or user_input == 'l':
        ready = True
      else:
        print('Please enter \'h\' or \'l''\'')
    
    return user_input

# highest level abstraction for the card game
class CardGame:
  score = 300
  is_playing = True

  # gets a random number from 1, 13
  def get_random_number(self):
    return random.randint(1, 13)

  # modifies score based on user input
  def run_score(self, h_or_l, rn1, rn2):
    if (h_or_l == 'l'):
      if (rn1 > rn2):
        self.score = self.score + 100
      else:
        self.score = self.score - 75
    else:
      if (rn1 < rn2):
        self.score = self.score + 100
      else:
        self.score = self.score - 75

  # starts the game
  def start(self):
    count = 0

    while self.is_playing:
      dealer_number = self.get_random_number()
      print(f'\nThe card is: {dealer_number}')

      validator = InputValidator()
      h_or_l = validator.get()

      next_card = self.get_random_number()
      print(f'The next card was: {next_card}')
      
      self.run_score(h_or_l, dealer_number, next_card)

      print(f'Your score is {self.score}')

      if (self.score > 0):
        keep_playing = input('Play again? [y/n] ')

        if (keep_playing != 'y'):
          self.is_playing = False
      else:
          self.is_playing = False
        
def main():
  game = CardGame()
  game.start()

main()
