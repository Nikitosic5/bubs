num = int(input("Введите число:"))
res = []
while num > 0:
    res.append(num %10)
    num = num // 10
    res = res[::-1]
print(sum(res))