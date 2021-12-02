#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
  lines = [l.rstrip().split(" ") for l in open(sys.argv[1]).readlines()]

  h, d, a = 0, 0, 0
  for cmd, val in lines:
    val = int(val)

    if cmd == "forward":
      d += (a * val)
      h += val

    elif cmd == "down":
      a += val

    elif cmd == "up":
      a -= val

  print(h * d)

main()
