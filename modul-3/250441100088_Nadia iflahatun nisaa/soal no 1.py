n = int(input("masukkan batas akhir:"))
print("bilangan prima dari 1 sampai", n, ":")
for i in range(2, n + 1):
    jumlah_faktor = 0
    for j in range(1, i + 1):
        if i % j == 0:
            jumlah_faktor = jumlah_faktor + 1
    if jumlah_faktor == 2:
        print(i)
