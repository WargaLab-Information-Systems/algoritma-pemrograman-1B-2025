n = int(input("masukkan angka n: ")) # inputan jumlah baris
    
for i in range(1, n + 1):
    for j in range(1, i + 1):   # sisi kiri piramida
        print(j, end=" ")
    for k in range((n - i) * 2 +1 ):        # spasi ditengah
        print(" ", end=" ")
    for j in range(i, 0, -1):   # sisi kanan piramida
        print(j, end=" ")
    print()
