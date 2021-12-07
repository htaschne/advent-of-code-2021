#!/usr/bin/env python3

import sys

from functools import lru_cache

def fuel(pos: int, lst: list[int]) -> int:
  acc = 0
  for h in lst:
    acc += abs(pos - h)
  return acc

@lru_cache
def s(x: int) -> int:
  return x * (1 + x) // 2

def inc_fuel(pos: int, lst: list[int]) -> int:
  acc = 0
  for h in lst:
    acc += s(abs(pos - h))
  return acc

def main():
  h = list(map(int, open(sys.argv[1]).readline().split(",")))
  print(min(fuel(i, h) for i in range(max(h))))
  print(min(inc_fuel(i, h) for i in range(max(h))))

main()
