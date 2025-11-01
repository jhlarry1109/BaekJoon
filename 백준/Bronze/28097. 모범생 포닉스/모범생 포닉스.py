import sys

input = sys.stdin.readline

N = int(input().strip())
T = list(map(int, input().split()))

total = sum(T) + 8 * (N - 1)
days = total // 24
hours = total % 24
print(days, hours)
