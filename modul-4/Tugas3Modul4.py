n = int(input("Masukkan jumlah baris:"))

# Perulangan untuk setiap baris
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")

    spasi =((n - i) * 2 +2 )
    for k in range(spasi):
        print(" ", end="")

    for i in range(i, 0, -1):
        print(i, end="")

    # Pindah ke baris berikutnya
    print()























