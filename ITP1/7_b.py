n_x = []
while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    else:
        n_x.append([n, x])

for line in n_x:
    n, x = line[0], line[1]
    res = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                if i + j + k == x:
                    res += 1
    print(res)
