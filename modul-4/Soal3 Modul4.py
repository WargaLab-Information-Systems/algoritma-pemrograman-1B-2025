# Program membuat dua piramida angka saling berhadapan (lancip di atas)

n = int(input("Masukkan tinggi piramida: "))

# Perulangan utama untuk setiap baris dari atas ke bawah
for i in range(n, 0, -1):

    # Perulangan pertama: mencetak sisi kiri piramida
    for j in range(1, i + 1):
        print(j, end="")

    # Perulangan kedua: mencetak spasi di tengah
    for j in range(2 * (n - i)):
        print(" ", end="")

    # Perulangan ketiga: mencetak sisi kanan piramida (cerminan)
    for j in range(i, 0, -1):
        print(j, end="")

    # Pindah ke baris berikutnya
    print()
