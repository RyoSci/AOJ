n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    for j in range(i, 0, -1):
        if a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
    print(*a)