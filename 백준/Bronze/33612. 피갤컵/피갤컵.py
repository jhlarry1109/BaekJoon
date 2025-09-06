n = int(input())

year, month = 2024, 8

for _ in range(n - 1):
    month += 7
    if month > 12:
        year += month // 12
        month %= 12
        if month == 0:
            month = 12
            year -= 1

print(year, month)
