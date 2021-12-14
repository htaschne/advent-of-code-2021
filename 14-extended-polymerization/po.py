#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from collections import Counter


def count_letters(pairs, template):
  c = Counter()
  for p in pairs:
    c[p[0]] += pairs[p]
  c[template[-1]] += 1

  return max(c.values()), min(c.values())


def step(pairs, rules):
  new_pairs = Counter()

  for p in pairs:
    new_pairs[p[0] + rules[p]] += pairs[p]
    new_pairs[rules[p] + p[1]] += pairs[p]

  return new_pairs


def simulate(pairs, rules, template, size):
  for s in range(size):
    pairs = step(pairs, rules)

  most, least = count_letters(pairs, template)
  print(most - least)


def main():
  template, b = open(sys.argv[1]).read().rstrip().split("\n\n")

  rules = {}
  for r in b.rstrip().split("\n"):
    f, t = r.split(" -> ")
    rules[f] = t

  pairs = Counter()
  for i in range(len(template) - 1):
    pairs[template[i] + template[i + 1]] += 1

  simulate(pairs, rules, template, 10)
  simulate(pairs, rules, template, 40)


main()
