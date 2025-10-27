import sys

for line in sys.stdin:
    if not line.strip():
        continue
    parts = line.split()
    for i in range(0, len(parts), 2):
        N = int(parts[i])
        S = int(parts[i+1])
        print(S // (N + 1))
