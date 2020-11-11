n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))


nums = []
for j in range(1 << n):
    res = 0
    for k in range(n):
        if j >> k & 1:
            res += a[k]
    nums.append(res)

for i in range(q):
    if m[i] in nums:
        print("yes")
    else:
        print("no")
