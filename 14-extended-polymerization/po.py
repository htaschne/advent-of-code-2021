#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from collections import defaultdict, Counter

def step(template, rules):
  pairs = list(zip(template, template[1:]))

  new_template = ""
  for p in pairs:
    f, t = p
    new_template += f + rules["".join(p)]

  p = pairs[-1]
  f, t = p
  new_template += t

  return new_template

def call(pair, rules, counter, s=0):
  # stop case
  if s == 40:
    counter[pair[0]] += 1
    counter[pair[1]] += 1
    return

  # generate two pairs from one
  p1 = pair[0] + rules[pair]
  p2 = rules[pair] + pair[1]

  # recursively call
  call(p1, rules, counter, s+1)
  call(p2, rules, counter, s+1)


def one(template, rules):
  for i in range(10):
    template = step(template, rules)
    # print(i, len(template))

  c = Counter(template)
  mn, mx = min([x for x in c.values()]), max([x for x in c.values()])
  print(mx - mn)

def main():
  template, b = open(sys.argv[1]).read().rstrip().split("\n\n")

  rules = {}
  for r in b.rstrip().split("\n"):
    f, t = r.split(" -> ")
    rules[f] = t

  one(template, rules)

  # too slow
  # counter = defaultdict(int)
  # for p in ["".join(x) for x in list(zip(template, template[1:]))]:
  #   call(p, rules, counter)
  # print(counter)

main()
