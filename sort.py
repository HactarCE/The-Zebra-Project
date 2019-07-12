#!/usr/bin/env python3

zebra_lines = []
with open('zebra.txt') as f:
    zebra_lines = sorted(f, key=lambda s: s.casefold())
with open('zebra.txt', 'w') as f:
    for line in zebra_lines:
        f.write(line)
