d = {}

def dfs(n):
    if n in d:
        return d[n]
    li = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a = i
            b = n//i
            li.append(max(dfs(a), dfs(b)))
    if li:
        d[n] = min(li) + 1
    else:
        d[n] = 0
    return d[n]
        
n = int(input())
print(dfs(n))