n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
li.sort()

dic = {}
for num in li:
    dic[num] = dic.get(num, 0)+1

m = max(dic.values())

bin = []
for num, count in dic.items():
    if count == m:
        bin.append(num)
bin.sort()
if len(bin) >= 2:
    bin = bin[1]
else:
    bin = bin[0]
if round(sum(li)/n) == -0:
    print(0)
else:
    print(f"{sum(li)/n:.0f}")
print(li[n//2])
print(bin)
print(max(li)-min(li))