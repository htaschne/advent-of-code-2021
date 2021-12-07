#!/usr/bin/env python3

import sys

def fuel(pos: int, lst: list[int]) -> int:
  return sum([abs(pos - h) for h in lst])

def s(x: int) -> int:
  return x * (1 + x) // 2

def inc_fuel(pos: int, lst: list[int]) -> int:
  return sum([s(abs(pos - h)) for h in lst])

def main():
  h = list(map(int, open(sys.argv[1]).readline().split(",")))
  print(min(fuel(i, h) for i in range(max(h))))
  print(min(inc_fuel(i, h) for i in range(max(h))))

main()
