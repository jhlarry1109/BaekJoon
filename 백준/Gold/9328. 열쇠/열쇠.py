from collections import deque

t = int(input())
for _ in range(t):
    li = []
    h,w = map(int,input().split())
    li.append(['.']*(w+2))
    for i in range(h):
        li.append(['.'] + list(input()) + ['.'])
    li.append(['.']*(w+2))
    k = input()
    visited = [[False for _ in range(w+2)] for _ in range(h+2)]
    queue = deque([[0,0]])
    door = [[] for _ in range(26)]
    visited[0][0] = True
    keys = [False] * 26
    if k != '0':
        for i in k:
            keys[ord(i)-ord('a')] = True
    cnt = 0
    while queue:
        x,y = queue.popleft()
        for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
            a,b = x+dx, y+dy
            if not(h+2 > a >= 0 and w+2 > b >= 0):
                continue
            if visited[a][b]:
                continue
        
            chk = li[a][b]
            if chk == '*':
                continue
            visited[a][b] = True
            if chk == '$':
                cnt += 1
                queue.append([a,b])
            elif 'a' <= chk <= 'z':
                idx = ord(chk) - ord('a')
                if keys[idx] == False:
                    keys[idx] = True
                    for ax, ay in door[idx]:
                        queue.append([ax, ay])
                        visited[ax][ay] = True
                    door[idx] = []
                queue.append([a,b])
            elif 'A' <= chk <= 'Z':
                idx = ord(chk) - ord('A')
                if keys[idx]:
                    queue.append([a,b])
                else:
                    door[idx].append([a,b])
            else:
                queue.append([a,b])
            
    print(cnt)