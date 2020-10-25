n = int(input())
r = [int(input()) for i in range(n)]
min_r = r[0]
res = r[1] - r[0]
for i in range(1, n):
    # print(res, min_r)
    res = max(res, r[i] - min_r)
    if min_r > r[i]:
        min_r = r[i]
print(res)
