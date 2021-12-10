#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def parse(s):
  stack = []
  for c in s:
    if c in '([{<':
      stack.append(c)
    elif c in ')]}>':
      if not stack:
        return c
      if c == ')' and stack[-1] == '(':
        stack.pop()
      elif c == ']' and stack[-1] == '[':
        stack.pop()
      elif c == '}' and stack[-1] == '{':
        stack.pop()
      elif c == '>' and stack[-1] == '<':
        stack.pop()

      elif c == ')' and stack[-1] in '[{<':
        return "corrupted", c
      elif c == ']' and stack[-1] in '({<':
        return "corrupted", c
      elif c == '}' and stack[-1] in '([<':
        return "corrupted", c
      elif c == '>' and stack[-1] in '({[':
        return "corrupted", c
      else:
        return c

  return "".join(stack)


def autocomplete(s):
  score = 0
  for i in reversed(s):
    score *= 5
    if i == '(':
      score += 1
    elif i == '[':
      score += 2
    elif i == '{':
      score += 3
    elif i == '<':
      score += 4

  return score


acc = 0
scores = []
for line in open(sys.argv[1]).readlines():
  line = line.strip()

  x = parse(line)
  if "corrupted" in x:
    if x[1] == ')':
      acc += 3
    elif x[1] == ']':
      acc += 57
    elif x[1] == '}':
      acc += 1197
    elif x[1] == '>':
      acc += 25137

  else:
    scores.append(autocomplete(x))

scores.sort()

print(acc)
print(scores[len(scores) // 2])
