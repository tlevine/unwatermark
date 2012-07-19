#!/usr/bin/env python
import sys

lines=sys.stdin.read().split('\n')
lines.reverse()

print '\n'.join(lines)
