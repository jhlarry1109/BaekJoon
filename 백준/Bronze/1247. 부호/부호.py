for _ in range(3):
    n = int(input())
    li = []
    for _ in range(n):
        li.append(int(input()))
    if sum(li) == 0:
        print("0")
    elif sum(li) > 0:
        print("+")
    else:
        print("-")