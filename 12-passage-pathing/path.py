#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from collections import defaultdict, Counter


def explore(target, G, path, paths, twice):
  if path in paths:
    return

  if target == "end":
    # print(",".join(path))
    paths.add(path)
    return

  for n in G[target]:
    c = Counter(path)
    if n.islower() and n in c and not (twice == n and c[n] < 2):
      continue

    explore(n, G, path + (n, ), paths, twice)


def main():
  small = set()
  G = defaultdict(list)
  for line in open(sys.argv[1]):
    s, e = line.rstrip().split("-")
    G[s].append(e)
    G[e].append(s)

    if s.islower() and s not in ("start", "end"):
      small.add(s)
    if e.islower() and e not in ("start", "end"):
      small.add(e)

  paths = set()
  for s in small:
    explore("start", G, ("start", ), paths, s)

  print(len(paths))


main()
