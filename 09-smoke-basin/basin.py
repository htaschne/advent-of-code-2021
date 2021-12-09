#!/usr/bin/env python3

import sys

DR, DC = (-1, 1, 0, 0), (0, 0, -1, 1)
marks = set()


def lowest(row, col, x, value):
  for dr, dc in zip(DR, DC):
    if (row + dr, col + dc) in x:
      if value >= x[(row + dr, col + dc)]:
        return False
  return True


def explore(n, x):
  global marks, DR, DC

  row, col = n
  if x[(row, col)] == 9:
    return 0

  marks.add((row, col))
  # print_map(row, col)

  acc = sum([
      explore((row + dr, col + dc), x) for dr, dc in zip(DR, DC)
      if (row + dr, col + dc) in x and (row + dr, col + dc) not in marks
  ])

  return acc + 1


def print_map(lines, row=-1, col=-1):
  if (row, col) == (-1, -1):
    for row, line in enumerate(open(sys.argv[1]).readlines()):
      print(line.rstrip())
    return

  for row, line in enumerate(open(sys.argv[1]).readlines()):
    print(line.rstrip())


def main():
  global marks
  lines = [
      list(map(int, list(line.rstrip())))
      for line in open(sys.argv[1]).readlines()
  ]

  x = {}
  for row, line in enumerate(open(sys.argv[1]).readlines()):
    for col, char in enumerate(line.rstrip()):
      x[(row, col)] = int(char)

  lo = set()
  acc = 0
  for row, line in enumerate(lines):
    for col, value in enumerate(line):
      if lowest(row, col, x, value):
        lo.add((row, col))
        acc += (1 + value)
  print(acc)

  sizes = sorted([explore(l, x) for l in lo], reverse=True)
  print(sizes[0] * sizes[1] * sizes[2])

  # print_map(lines)


main()
