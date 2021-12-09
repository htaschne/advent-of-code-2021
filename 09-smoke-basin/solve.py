#!/usr/bin/env python3

import sys

def lowest(row, col, x, value):
  for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    if (row+dr, col+dc) in x:
      if value >= x[(row+dr, col+dc)]:
        return False
  return True


marks = set()
def explore(n, x):
  global marks

  row, col = n
  if x[(row, col)] == 9:
    return 0

  marks.add((row, col))

  acc = 0
  for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    if (row+dr, col+dc) in x and (row+dr, col+dc) not in marks:
      acc += explore((row+dr, col+dc), x)

  return acc + 1
  

def main():
  global marks
  lines = [list(map(int, list(line.rstrip()))) for line in open(sys.argv[1]).readlines()]

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

  sizes = []
  for l in lo:
    sizes.append(explore(l, x))
  sizes = sorted(sizes, reverse=True)
  print(sizes[0] * sizes[1] * sizes[2])


main()
