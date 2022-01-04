#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from dijkstar import Graph, find_path


def expand(edges, mr, mc):
  new_edges = {}

  for tile_row in range(5):
    for tile_col in range(5):
      for i in range(mr):
        for j in range(mc):
          new_risk = edges[(i, j)] + tile_row + tile_col

          if new_risk > 9:
            new_risk -= 9

          assert new_risk <= 9

          new_edges[(tile_row * mr + i, tile_col * mc + j)] = new_risk

  return new_edges


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

  min_path = find_path(g, (0, 0), (mr, mc)).total_cost
  print(min_path)

  edges = expand(edges, mr + 1, mc + 1)

  g = Graph()
  for r, c in edges:
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      row = r + dr
      col = c + dc
      if (row, col) in edges:
        w = edges[(row, col)]
        g.add_edge((r, c), (row, col), w)

  min_path = find_path(g, (0, 0), ((mr * 5) + 4, (mc * 5) + 4)).total_cost
  print(min_path)


main()
