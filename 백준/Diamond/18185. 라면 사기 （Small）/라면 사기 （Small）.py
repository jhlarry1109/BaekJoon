n = int(input())
a = list(map(int, input().split()))

cost = 0

for i in range(n-2):
    if a[i+1] > a[i+2]:
        two = min(a[i], a[i+1] - a[i+2])
        a[i] -= two
        a[i+1] -= two
        cost += 5 * two

        three = min(a[i], a[i+1], a[i+2])
        a[i] -= three
        a[i+1] -= three
        a[i+2] -= three
        cost += 7 * three

    else:
        three = min(a[i], a[i+1], a[i+2])
        a[i] -= three
        a[i+1] -= three
        a[i+2] -= three
        cost += 7 * three

        two = min(a[i], a[i+1])
        a[i] -= two
        a[i+1] -= two
        cost += 5 * two

    cost += 3 * a[i]
    a[i] = 0

if a[n-2] > 0 and a[n-1] > 0:
    two = min(a[n-2], a[n-1])
    a[n-2] -= two
    a[n-1] -= two
    cost += 5 * two

cost += 3 * a[n-2]
cost += 3 * a[n-1]

print(cost)