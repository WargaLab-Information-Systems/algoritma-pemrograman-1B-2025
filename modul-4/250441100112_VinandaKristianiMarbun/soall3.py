# Program membuat dua piramida angka saling berhadapan (cermin)

# Meminta input dari pengguna
n = int(input("Masukkan angka: "))

# Perulangan untuk setiap baris
for i in range(1, n + 1):
    # Bagian kiri piramida
    for j in range(1, i + 1):
        print(j, end=" ")

    # Spasi di tengah (semakin kecil tiap baris)
    print("  " * (n - i), end="")

    # Bagian kanan piramida (cermin)
    for j in range(i, 0, -1):
        print(j, end=" ")

    # Pindah ke baris berikutnya
    print()