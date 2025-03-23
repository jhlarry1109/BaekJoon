a = int(input())
b = int(input())
c = int(input())
n = a*b*c
n = str(n)
dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
for i in range(10):
    ans = 0
    for j in n:
        if dic[j] == i:
            ans += 1
    print(ans)