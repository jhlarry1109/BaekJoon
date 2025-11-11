S = input().strip()
target = "SciComLove"

count = 0
for a, b in zip(S, target):
    if a != b:
        count += 1

print(count)
