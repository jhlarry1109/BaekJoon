import sys

S = int(sys.stdin.readline().strip())
F = int(sys.stdin.readline().strip())

if F < S:
    print("flight")
else:
    print("high speed rail")
