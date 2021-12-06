#!/usr/bin/env python3

import sys

def step(jellys):
  to_append = []
  new_jellys = []
  for j in jellys:
    if j == 0:
      new_jellys.append(6)
      to_append.append(8)
    else:
      new_jellys.append(j - 1)
  return new_jellys + to_append


def main():
  jellys = list(map(int, open(sys.argv[1]).readline().rstrip().split(",")))

  for _ in range(80):
    jellys = step(jellys)

  print(len(jellys))


main()
