n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

# TLEになった
# for i in range(q):
#     ans = False
#     for j in range(1 << n):
#         res = 0
#         for k in range(n):
#             if j >> k & 1:
#                 res += a[k]
#             if res == m[i]:
#                 ans = True
#                 break
#         if ans:
#             break
#     if ans:
#         print("yes")
#     else:
#         print("no")


nums = set()
for j in range(1 << n):
    res = 0
    for k in range(n):
        if j >> k & 1:
            res += a[k]
    nums.add(res)

for i in range(q):
    if m[i] in nums:
        print("yes")
    else:
        print("no")
