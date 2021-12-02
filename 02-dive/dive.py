#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
  lines = [l.rstrip().split(" ") for l in open(sys.argv[1]).readlines()]

  h, d, a = 0, 0, 0
  for cmd, val in lines:
    val = int(val)

    match cmd:
      case "forward":
        d += (a * val)
        h += val

      case "down":
        a += val

      case "up":
        a -= val

  print(h * d)

main()
