#!/usr/bin/env python3

import sys

from collections import defaultdict

def step(jellys: dict[int, int]) -> dict[int, int]:
  new_jellys = defaultdict(int)
  for n, count in jellys.items():
    if n == 0:
      new_jellys[6] += count
      new_jellys[8] += count
    else:
      new_jellys[n - 1] += count

  return new_jellys


def main():
  list_jellys = list(map(int, open(sys.argv[1]).readline().rstrip().split(",")))
  jellys = defaultdict(int)

  for j in list_jellys:
    jellys[j] += 1

  for day in range(256):
    jellys = step(jellys)

  print(sum(jellys.values()))


main()
