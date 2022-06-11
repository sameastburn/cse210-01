# Tic-Tac-Toe
# sameastburn

game = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

def print_game():
  print(game[0][0], '|', game[0][1], '|', game[0][2])
  print('-+-+-+-+-')
  print(game[1][0], '|', game[1][1], '|', game[1][2])
  print('-+-+-+-+-')
  print(game[2][0], '|', game[2][1], '|', game[2][2])

def replace_square(spot, turn):
  for num_list in game:
    if (num_list[0] == spot):
      num_list[0] = turn
    elif (num_list[1] == spot):
      num_list[1] = turn
    elif (num_list[2] == spot):
      num_list[2] = turn

def is_draw():
  count = 0

  for i in range(3):
    for o in range(3):
      if (game[i][o] == 'x' or game[i][o] == 'o'):
        count = count + 1
  
  return count == 9

def did_win():
  win = ''
  
  for i in range(3):
    if (game[i][0] == game[i][1] == game[i][2]):
      win = game[i][0]

  for i in range(3):
    if (game[0][i] == game[1][i] == game[2][i]):
      win = game[0][i]

  if (game[0][0] == game[1][1] == game[2][2]):
    win = game[0][i]

  if (game[0][2] == game[1][1] == game[2][0]):
      win = game[0][i]

  return win

def main():
  print_game()

  turn = 'x'
  end = False
  count = 0

  while (not end):
    square = int(input(f'\n{turn}\'s turn to choose a square (1-9): '))
    
    replace_square(square, turn)

    turn = 'o' if turn == 'x' else 'x'

    if (did_win() or is_draw()):
      print('\n...\n')
      print_game()
      print('\nGood game. Thanks for playing!')
      end = True
    else:
      print('')
      print_game()

main()
