#!/usr/bin/env python

import sys

def fuel(pos, lst):
  acc = 0
  for h in lst:
    acc += abs(pos - h)
  return acc

def main():
  h = list(map(int, open(sys.argv[1]).readline().split(",")))
  print(h)

  best = 10000000
  for i in range(max(h)):
    best = min(fuel(i, h), best)
  print(best)


main()
