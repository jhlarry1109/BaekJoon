sum = 0
cnt = 0
for _ in range(5):
    n = int(input())
    if n < 40:
        n = 40
    sum += n
print(sum//5)