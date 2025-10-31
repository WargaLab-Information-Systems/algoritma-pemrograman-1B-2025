n = int(input("Masukkan jumlah baris (n): "))

for i in range(1, n + 1):
    # --- sisi kiri piramida ---
    for j in range(1, i + 1):
        print(j, end[""])

    # --- ruang kosong di tengah ---
    spasi = (n - i) * 2 + 3
    for k in range(spasi):
        print(" ", end=" ")

    # --- sisi kanan piramida (cermin) ---
    for l in range(i, 0, -1):
        print(l, end=" ")

    print()  
