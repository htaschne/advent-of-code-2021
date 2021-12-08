#!/usr/bin/env python3

import sys

from collections import defaultdict

def main():
  d = defaultdict(list)
  for line in open(sys.argv[1]).readlines():
    b, a = line.split(" | ")
    words = a.split()

    for w in words:
      d[len(w)].append(w)
  
  acc = 0
  for k, v in d.items():
    if k == 2: # 1
      acc += len(v)
    elif k == 3: # 7
      acc += len(v)
    elif k == 4: # 4
      acc += len(v)
    elif k == 7: # 8
      acc += len(v)

  print(acc)

main()
