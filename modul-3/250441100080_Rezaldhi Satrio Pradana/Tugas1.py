angka = int(input("Masukkan batas angka: "))
for n in range(2, angka + 1):
    faktor = 0
    for i in range(1, n + 1):
        if n % i == 0:
            faktor += 1
if faktor == 2:
    print(n, "adalah bilangan prima")