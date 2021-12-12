#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from collections import defaultdict

def explore(target, G, path, paths):
  if target == "end":
    paths.add(path)
    # print(",".join(path))
    return 1

  if path in paths:
    return 0

  ways = 0
  for n in G[target]:
    if n.islower() and n in set(path):
      continue

    ways += explore(n, G, path + (n, ), paths)
  return ways


def main():
  G = defaultdict(list)
  for line in open(sys.argv[1]):
    s, e = line.rstrip().split("-")
    G[s].append(e)
    G[e].append(s)

  paths = set()
  total = explore("start", G, ("start", ), paths)
  print(total)

main()
