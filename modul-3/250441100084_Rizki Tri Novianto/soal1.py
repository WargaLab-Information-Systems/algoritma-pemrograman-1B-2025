n = int(input("Masukkan nilai n: "))
print("Bilangan prima:",end=' ' )

i = 2
while i <= n:
    pembagi = 0
    k = 1
    while k <= i:
        if i % k == 0:
            pembagi += 1
        k += 1
    if pembagi == 2:
        print(i, end=' ')
    i += 1
