n = int(input())
stack = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if stack:
            stack.pop()
    else:
        stack.append(num)

print(sum(stack))