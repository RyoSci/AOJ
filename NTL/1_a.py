n = int(input())
n1 = n
res = []
div = 2
while True:
    if n % div == 0:
        n //= div
        res.append(str(div))
    else:
        div += 1

    if n == 1:
        break
    if div > int(n1 ** 0.5):
        res.append(str(n))
        break

print(str(n1) + ": " + " ".join(res))
