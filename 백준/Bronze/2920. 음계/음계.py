a = list(map(int,input().split()))
b = sorted(a)
c = b[::-1]

if a == b:
    print("ascending")
elif a == c:
    print("descending")
else:
    print("mixed")