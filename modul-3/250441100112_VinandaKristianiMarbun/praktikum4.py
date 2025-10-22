while True:
    nama_pembeli = input("Masukkan nama pembeli: ")

    daftar_barang = []
    total = 0

    while True:
        barang = input("Nama barang: ")
        harga = float(input("Harga barang: "))
        daftar_barang.append((barang, harga))
        total += harga

        lagi = input("Tambah barang lagi? (y/n): ")
        if lagi.lower() == "n":
            break

    print("=== STRUK PEMBELIAN INDOMEI ===")
    print(f"Nama Pembeli : {nama_pembeli}")
    print(f"Total Harga   : Rp{total:,.0f}")
    print("Terima kasih telah berbelanja di IndoMei.\n")

    pembeli_berikutnya = input("Apakah ada pembeli berikutnya? (y/n): ")
    if pembeli_berikutnya == "n":
        print("Program selesai.")
        break
