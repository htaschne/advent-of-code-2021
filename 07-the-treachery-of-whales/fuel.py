#!/usr/bin/env python

import sys

def fuel(pos, lst):
  acc = 0
  for h in lst:
    acc += abs(pos - h)
  return acc

def inc_fuel(pos, lst):
  acc = 0
  for h in lst:
    move_cost = 1
    for i in range(abs(pos - h)):
      acc += move_cost
      move_cost += 1
  return acc

def main():
  h = list(map(int, open(sys.argv[1]).readline().split(",")))

  best = 10000000000000
  for i in range(max(h)):
    best = min(fuel(i, h), best)
  print(best)

  best = 10000000000000
  for i in range(max(h)):
    best = min(inc_fuel(i, h), best)
  print(best)


main()
