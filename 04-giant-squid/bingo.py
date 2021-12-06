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

  def mark(self, token: int) -> bool:
    if token not in self.positions:
      return False

    row, col = self.positions[token]
    self.marks[(row, col)] = True
    return self.check_winner(row, col)

  def print(self):
    for r, row in enumerate(self.board):
      for c, col in enumerate(row):
        if self.marks[(r, c)]:
          print("\033[32m" + "%2d" % col + "\033[0m", end=" ")
        else:
          print("%2d" % col, end=" ")
      print()

  def score(self, token: int) -> int:
    return token * sum([self.board[k[0]][k[1]] for k, v in self.marks.items() if not v])


@dataclass
class Game:
  boards: list[Board]
  draws: list[int]

  def pick(self, token: int) -> (bool, list[list[int]]):
    ret = []
    for i, board in enumerate(self.boards):
      if i not in self.winners:
        if board.mark(token):
          ret.append((i, self.boards[i].score(token)))
    if len(ret) == 0:
      return False, [[-1, -1]]
    return True, ret

  def play(self):
    self.winners = set()
    has_winner, score = False, -1
    for draw in self.draws:
      has_winner, round_winners = self.pick(draw)

      if has_winner:
        for winner, score in round_winners:
          if winner not in self.winners:
            self.winners.add(winner)
            b = self.boards[winner]
            b.print()
            print(f"board winner: {winner + 1} with score = {score}")
            print()


def read_case(filename: str) -> Game:
  content = open(filename).read().split("\n\n")
  draws = list(map(int, content[0].split(",")))
  boards = [Board([list(map(int, x.strip().replace("  ", " ").split(" "))) for x in b.split("\n") if x]) for b in content[1:]]
  return Game(boards, draws)


def main():
  game = read_case(sys.argv[1])
  game.play()


main()
