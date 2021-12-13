#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def pp(points):
  x0 = min([p[0] for p in points])
  xm = max([p[0] for p in points])

  y0 = min([p[1] for p in points])
  ym = max([p[1] for p in points])

  for y in range(y0, ym+1):
    for x in range(x0, xm+1):
      if (x, y) in points:
        print("█", end="")
      else:
        print(" ", end="")
    print()

def fold(points, ax, val):
  new_points = set()
  if ax == "y":
    for p in points:
      if p[1] > val:
        dist = abs(p[1] - val)
        new_points.add((p[0], p[1] - 2 * dist))
      else:
        new_points.add(p)

  else:
    for p in points:
      if p[0] > val:
        dist = abs(p[0] - val)
        new_points.add((p[0] - 2 * dist, p[1]))
      else:
        new_points.add(p)

  return new_points

def main():
  a, b = open(sys.argv[1]).read().split("\n\n")

  points = set(tuple(map(int, l.rstrip().split(","))) for l in a.split("\n"))
  folds = [x.rstrip() for x in b.rstrip().split("\n")]

  ax, val = folds[0].split()[-1].split("=")
  val = int(val)

  print(len(fold(points, ax, val)), end="\n\n")

  for f in folds:
    ax, val = f.rstrip().split()[-1].split("=")
    val = int(val)

    points = fold(points, ax, val)

  pp(points)


main()
