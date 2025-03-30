n, m = map(int,input().split())
card = list(map(int,input().split()))
li = []

for i in range(n-1):
    for j in range(i+1, n):
        for k in range(j+1, n):
            li.append(card[i] + card[j] + card[k])
            if card[i] + card[j] + card[k] == m:
                print(m)
                exit()
li.sort(reverse=True)
for i in range(len(li)):
    if li[i] < m:
        print(li[i])
        break