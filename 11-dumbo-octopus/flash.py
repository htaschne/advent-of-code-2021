#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from collections import deque


def step(energy_levels):
  changed = set()
  for row in range(len(energy_levels)):
    for col in range(len(energy_levels[row])):
      energy_levels[row][col] += 1
      if energy_levels[row][col] > 9:
        changed.add((row, col))

  Q = deque(changed)
  for row, col in changed:
    energy_levels[row][col] = 0

  while Q:
    row, col = Q.popleft()
    for r, c in [(row - 1, col), (row + 1, col), (row, col - 1),
                 (row, col + 1), (row - 1, col - 1), (row + 1, col + 1),
                 (row - 1, col + 1), (row + 1, col - 1)]:

      if (r, c) in changed:
        continue
      if r < 0 or r >= len(energy_levels) or c < 0 or c >= len(energy_levels[r]):
        continue

      energy_levels[r][c] += 1
      if energy_levels[r][c] > 9:
        Q.append((r, c))
        changed.add((r, c))
        energy_levels[r][c] = 0

  return len(changed)


def shy(energy_levels):
  for row in energy_levels:
    for level in row:
      if level == 0:
        print('\x1b[30;42m' + str(level) + '\x1b[0m', end="")
      else:
        print(level, end="")
    print()
  print()


def main():
  energy_levels = [[int(c) for c in line.rstrip()]
                   for line in open(sys.argv[1])]

  acc = 0
  for s in range(100):
    acc += step(energy_levels)
  print(acc)

  s = 100
  while step(energy_levels) != len(energy_levels) * len(energy_levels[0]):
    s += 1
  print(s + 1)


main()
