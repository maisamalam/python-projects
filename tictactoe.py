from typing import List, Tuple

def print_board(board: List[List[str]]) -> None:

  for row in board:
    print(' '.join(row))

def get_empty_spaces(board: List[List[str]]) -> List[Tuple[int, int]]:

  empty_spaces = []
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == ' ':
        empty_spaces.append((i, j))
  return empty_spaces

def get_winner(board: List[List[str]]) -> str:

  for row in board:
    if row.count(row[0]) == len(row) and row[0] != ' ':
      return row[0]
  for col in range(len(board)):
    if board[0][col] != ' ' and all(board[row][col] == board[0][col] for row in range(len(board))):
      return board[0][col]

  if board[0][0] != ' ' and all(board[i][i] == board[0][0] for i in range(len(board))):
    return board[0][0]
  if board[0][-1] != ' ' and all(board[i][len(board)-1-i] == board[0][-1] for i in range(len(board))):
    return board[0][-1]
  if not any(space == ' ' for row in board for space in row):
    return 'T'
  return ''
def play_tic_tac_toe() -> None:

  board = [[' ' for _ in range(3)] for _ in range(3)]
  player = 'X'
  while True:
    print_board(board)
    row = int(input('Enter row: '))
    col = int(input('Enter col: '))
    if board[row][col] != ' ':
      print('Invalid move!')
      continue
    board[row][col] = player
    winner = get_winner(board)
    if winner:
      print_board(board)
      if winner == 'T':
        print('It\'s a draw!')
      else:
        print(f'{winner} won!')
      break
    player = 'O' if player == 'X' else 'X'

# play a game of tic-tac-toe
play_tic_tac_toe()