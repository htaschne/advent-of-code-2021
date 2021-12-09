#!/usr/bin/env python3

import sys

from collections import defaultdict


def main():
  d = defaultdict(int)
  for line in open(sys.argv[1]).readlines():
    a, b = line.rstrip().split(" -> ")
    r1, c1 = list(map(int, a.split(",")))
    r2, c2 = list(map(int, b.split(",")))

    if r1 != r2 and c1 != c2:
      # diagonal
      dr = 1 if r2 - r1 > 0 else -1
      dc = 1 if c2 - c1 > 0 else -1

      while r1 != r2 and c1 != c2:
        d[(r1, c1)] += 1
        r1 += dr
        c1 += dc

    if c1 == c2:
      r1, r2 = min(r1, r2), max(r1, r2)
      for row in range(r1, r2 + 1):
        d[(row, c1)] += 1

    elif r1 == r2:
      c1, c2 = min(c1, c2), max(c1, c2)
      for col in range(c1, c2 + 1):
        d[(r1, col)] += 1

  acc = 0
  for (row, col), count in d.items():
    if count >= 2:
      acc += 1
  print(acc)


main()
