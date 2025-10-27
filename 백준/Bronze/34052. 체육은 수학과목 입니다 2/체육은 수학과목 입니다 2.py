sum = 0
for _ in range(4):
    sum += int(input())
sum += 300
if sum <= 1800:
    print("Yes")
else:
    print("No")