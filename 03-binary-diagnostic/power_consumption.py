#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from collections import defaultdict, deque

def count_most(lines):
  dd = defaultdict(list)
  for l in lines:
    for i, d in enumerate(l):
      dd[i].append(int(d))

  mm = {}
  for k, v in dd.items():
    one = sum([x == 1 for x in v])
    zer = sum([x == 0 for x in v])

    most = "1" if one >= zer else "0"
    mm[k] = most

  return mm


def find_most(lines):
  i = 0
  while len(lines) > 1:
    mm = count_most(lines)
    new_lines = []

    for line in lines:
      if line[i] == mm[i]:
        new_lines.append(line)

    lines = new_lines
    i += 1

  return int(lines[0], 2)


def count_least(lines):
  dd = defaultdict(list)
  for l in lines:
    for i, d in enumerate(l):
      dd[i].append(int(d))

  ll = {}
  for k, v in dd.items():
    one = sum([x == 1 for x in v])
    zer = sum([x == 0 for x in v])

    least = "0" if one >= zer else "1"
    ll[k] = least

  return ll


def find_least(lines):
  i = 0
  while len(lines) > 1:
    mm = count_least(lines)
    new_lines = []

    for line in lines:
      if line[i] == mm[i]:
        new_lines.append(line)

    lines = new_lines
    i += 1

  return int(lines[0], 2)


def main():
  lines = [l.rstrip() for l in open(sys.argv[1]).readlines()]

  dd = defaultdict(list)
  for l in lines:
    for i, d in enumerate(l):
      dd[i].append(int(d))

  gamma, epsilon = "0b", "0b"
  for k, v in dd.items():
    one = sum([x == 1 for x in v])
    zer = sum([x == 0 for x in v])

    most = "1" if one > zer else "0"
    least = "0" if one > zer else "1"

    gamma += most
    epsilon += least


  print(int(gamma, 2) * int(epsilon, 2))

  oxygen = find_most(lines)
  co2 = find_least(lines)

  print(oxygen * co2)


main()
