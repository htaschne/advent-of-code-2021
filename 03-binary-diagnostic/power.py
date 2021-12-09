#!/usr/bin/env python3

import sys


def count_frequency(report: list[str]) -> list[int]:
  count = [0] * len(report[0])
  for diagnostic in report:
    for i, bit in enumerate(diagnostic):
      count[i] += int(bit)

  return count


def cast_and_inverse(n: str) -> (int, int):
  size, n = len(n), int(n, 2)
  return n, (1 << size) - 1 - n


def filter(report: list[str], a: str, b: str) -> int:
  i = 0
  while len(report) > 1:
    filtered_report = []
    count = count_frequency(report)

    for diagnostic in report:
      filtered_report = [
          d for d in report
          if d[i] == (a if count[i] >= len(report) / 2 else b)
      ]

    report = filtered_report
    i += 1

  return int(report[0], 2)


def main():
  report = [l.rstrip() for l in open(sys.argv[1])]
  count = count_frequency(report)

  gamma = ""
  for bit in count:
    gamma += "1" if bit > (len(report) / 2) else "0"

  gamma, epsilon = cast_and_inverse(gamma)
  print(gamma * epsilon)

  oxygen = filter(report, "1", "0")
  co2 = filter(report, "0", "1")

  print(oxygen * co2)


main()
