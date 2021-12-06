#!/usr/bin/env python3

import sys

from dataclasses import dataclass

class Board:

  def __init__(self, board: list[list[int]]):
    self.board = board
    self.positions: dict[int, (int, int)] = {}
    self.marks: dict[(int, int), bool] = {}

    for row in range(len(self.board)):
      for col in range(len(self.board[0])):
        token = self.board[row][col]
        self.positions[token] = (row, col)
        self.marks[(row, col)] = False

  def check_winner(self, row: int, col: int) -> bool:
    full_row = all(self.marks[(row, c)] for c in range(len(self.board[0])))
    full_col = all(self.marks[(r, col)] for r in range(len(self.board)))
    return full_row or full_col

  def mark(self, token: int):
    if token not in self.positions:
      return False

    row, col = self.positions[token]
    self.marks[(row, col)] = True
    return self.check_winner(row, col)

  def __str__(self) -> str:
    ret = "\n".join([str(row) for row in self.board])
    return ret+"\n"

  def score(self, token: int) -> int:
    return token * sum([self.board[k[0]][k[1]] for k, v in self.marks.items() if not v])


@dataclass
class Game:
  boards: list[Board]
  draws: list[int]

  def pick(self, token):
    for i, board in enumerate(self.boards):
      if board.mark(token):
        return True, i + 1, self.boards[i].score(token)
    return False, -1, -1

  def play(self):
    has_winner, score = False, -1
    for draw in self.draws:
      has_winner, winner, score = self.pick(draw)
      if has_winner:
        break
    print(f"board winner: {winner} with score = {score}")


def read_case(filename: str) -> Game:
  content = open(filename).read().split("\n\n")
  draws = list(map(int, content[0].split(",")))
  boards = [Board([list(map(int, x.strip().replace("  ", " ").split(" "))) for x in b.split("\n") if x]) for b in content[1:]]
  return Game(boards, draws)


def main():
  game = read_case(sys.argv[1])
  game.play()


main()
