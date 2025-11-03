N = int(input())
levels = [int(input()) for _ in range(N)]

first = levels[0]

if first == min(levels):
    print("ez")
elif first == max(levels):
    print("hard")
else:
    print("?")
