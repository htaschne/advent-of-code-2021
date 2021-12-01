#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

dps = [int(l.rstrip()) for l in open(sys.argv[1]).readlines()]

print(sum([1 for i in range(len(dps) - 1) if dps[i] < dps[i + 1]]))
print(sum([1 for i in range(len(dps) - 3) if dps[i] + dps[i+1] + dps[i+2] < dps[i+1]+ dps[i+2] + dps[i+3]]))
