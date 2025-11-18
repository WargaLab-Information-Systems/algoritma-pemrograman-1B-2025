print("Program Struk Pembelian IndoMei")

while True:
    nama = input("Nama pembeli: ")
    total = 0
    list_barang = []

    while True:
        barang = input("Nama barang (klik selesai jika sudah): ")
        if barang == "selesai":
            break
        harga = int(input("Harga barang: Rp "))
        list_barang += [(barang, harga)]
        total += harga

    print("\n STRUK PEMBELIAN")
    print("Nama pembeli:", nama)
    for b, h in list_barang:
        print("-", b, ": Rp", h)
    print("Total harga: Rp", total)
    print("Terima kasih sudah belanja di IndoMei\n")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lanjut != "y":
        print("Program selesai.")
        break
