#!/usr/bin/env python3

import sys

from collections import defaultdict


def decode(d: dict[int, list[str]]) -> dict[str, int]:
  assert (len(d[2]) == 1 and len(d[3]) == 1 and len(d[4]) == 1 and len(d[7]))
  one, four, seven, eight = d[2][0], d[4][0], d[3][0], d[7][0]

  three = [n for n in d[5] if set(one).issubset(set(n))][0]

  mid = set(three).intersection(set(four)) - set(one)

  zero = [s for s in d[6] if set(eight) - set(s) == mid][0]
  nine = [s for s in d[6] if set(one).issubset(set(s)) and s != zero][0]
  six = [s for s in d[6] if s != nine and s != zero][0]

  mu = set(four) - set(one)
  five = [s for s in d[5] if mu.issubset(set(s)) and s != three][0]
  two = [s for s in d[5] if s not in (three, five)][0]

  return {
      "".join(sorted(zero)): 0,
      "".join(sorted(one)): 1,
      "".join(sorted(two)): 2,
      "".join(sorted(three)): 3,
      "".join(sorted(four)): 4,
      "".join(sorted(five)): 5,
      "".join(sorted(six)): 6,
      "".join(sorted(seven)): 7,
      "".join(sorted(eight)): 8,
      "".join(sorted(nine)): 9
  }


def main():
  nacc = 0
  d = defaultdict(list)
  for line in open(sys.argv[1]).readlines():
    dd = defaultdict(list)
    b, a = line.split(" | ")
    words = a.split()
    nums = b.split()

    for w in words:
      d[len(w)].append(w)

    for w in nums:
      dd[len(w)].append(w)

    conv = decode(dd)

    s = ""
    for w in words:
      w = "".join(sorted(w))
      s += str(conv[w])

    nacc += int(s)

  acc = 0
  # rest = 2, 3, 5, 6, 9
  for k, v in d.items():
    if k == 2:  # 1
      acc += len(v)
    elif k == 3:  # 7
      acc += len(v)
    elif k == 4:  # 4
      acc += len(v)
    elif k == 7:  # 8
      acc += len(v)

  print(acc)
  print(nacc)


main()
