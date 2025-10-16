ulang = "y"

while ulang == "y":
    nama = input("Masukkan nama pembeli: ")
    total = 0
    lagi = "y"

    print("\nDaftar pembelian:")

    while lagi == "y":
        barang = input("Masukkan nama barang: ")
        harga = int(input("Masukkan harga barang: "))
        total = total + harga
        lagi = input("Apakah ingin menambah barang lagi? (y/n): ")

    print("\n===== STRUK PEMBELIAN INDO MEI =====")
    print("Nama Pembeli:", nama)
    print("Total harga seluruh barang: Rp", total)
    print("Terima kasih telah berbelanja di IndoMei.\n")

    ulang = input("Apakah ada pembeli berikutnya? (y/n): ")

