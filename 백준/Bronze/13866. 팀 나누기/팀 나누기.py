A, B, C, D = map(int, input().split())

diff1 = abs(A + B - (C + D))
diff2 = abs(A + C - (B + D))
diff3 = abs(A + D - (B + C))

print(min(diff1, diff2, diff3))
