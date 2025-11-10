N, W, H, L = map(int, input().split())
cols = W // L
rows = H // L
max_cows = cols * rows
print(min(N, max_cows))
