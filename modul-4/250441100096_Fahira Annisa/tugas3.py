n = int(input("Masukkan nilai n:"))

for i in range(1, n +1):
    # Sisi kiri piramida
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Ruang kosong di tengah
    for k in range ((n - i) * 2):
        print(" ", end=" ")

    # Sisi kanan piramida
    for j in range(i, 0, -1):
        print(j, end=" ")

    
    # Pindah ke baris berikutnya
    print()
