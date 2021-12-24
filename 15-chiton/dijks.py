#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from dijkstar import Graph, find_path

def main():

  edges = {}
  mr, mc = 0, 0
  for r, row in enumerate(open(sys.argv[1]).readlines()):
    for c, col in enumerate(row.strip()):
      edges[(r, c)] = int(col)
      mc = max(mc, c)
    mr = max(mr, r)

  g = Graph()
  for r, c in edges:
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      row = r + dr
      col = c + dc
      if (row, col) in edges:
        w = edges[(row, col)]
        g.add_edge((r, c), (row, col), w)

  ret = find_path(g, (0, 0), (mr, mc))
  print(ret)

main()
