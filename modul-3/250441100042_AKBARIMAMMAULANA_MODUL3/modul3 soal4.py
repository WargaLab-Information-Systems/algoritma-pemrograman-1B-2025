# Program menampilkan struk pembelian sederhana menggunakan perulangan

while True:
    nama_pembeli = input("Masukkan nama pembeli: ")
    total = 0
    daftar_barang = []

    while True:
        nama_barang = input("Masukkan nama barang: ")
        harga = float(input("Masukkan harga barang: "))
        jumlah = int(input("Masukkan jumlah barang: "))

        subtotal = harga * jumlah
        daftar_barang.append((nama_barang, harga, jumlah, subtotal))
        total += subtotal

        lagi = input("Apakah ingin menambah barang lagi? (y/n): ")
        if lagi.lower() != 'y':
            break

    print("\n========= STRUK PEMBELIAN =========")
    print("Nama Pembeli :", nama_pembeli)
    print("-----------------------------------")
    for barang, harga, jumlah, subtotal in daftar_barang:
        print(f"{barang} ({jumlah} x {harga:.0f}) = Rp{subtotal:.0f}")
    print("-----------------------------------")
    print(f"Total Harga : Rp{total:.0f}")
    print("Terima kasih telah berbelanja di IndoMei!")
    print("===================================\n")

    pembeli_berikut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if pembeli_berikut.lower() != 'y':
        print("Program selesai. Terima kasih.")
        break