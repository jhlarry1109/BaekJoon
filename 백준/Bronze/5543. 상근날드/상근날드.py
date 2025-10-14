li_1 = []
li_2 = []
for _ in range(3):
    li_1.append(int(input()))
for _ in range(2):
    li_2.append(int(input()))
sum = 0
sum += min(li_1)
sum += min(li_2)
print(sum-50)