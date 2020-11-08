m, n = map(int, input().split())
mod = 10 ** 9 + 7
div = 10 ** 4
quotient = n // div
remainder = n % div

m_dash = 1
for i in range(div):
    m_dash = (m_dash * m) % mod

res = 1
for i in range(quotient):
    res = (res * m_dash) % mod

for i in range(remainder):
    res = (res * m) % mod

print(res)
