m, n = map(int, input().split())
mod = 10 ** 9 + 7

res = m
res_1 = 1


def power(x: int, n: int):
    global res, res_1
    if n == 1:
        return res, res_1
    res = x * x % mod
    if n % 2 == 1:
        res_1 = res_1 * x % mod
    power(x * x % mod, n // 2)
    return res, res_1


m, n = power(m, n)
print(m * n % mod)
