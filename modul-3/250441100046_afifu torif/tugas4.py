while True:
    nama_pembeli = input("Masukkan nama pembeli: ")
    total = 0
    daftar_barang = []

    while True:
        barang = input("Nama barang (atau ketik 'selesai' untuk selesai): ")
        if barang.lower() == 'selesai':
            break
        harga = float(input(f"Harga {barang}: Rp "))
        daftar_barang.append((barang, harga))
        total += harga

    print("\n=== STRUK PEMBELIAN INDOMEI ===")
    print("Nama pembeli :", nama_pembeli)
    for barang, harga in daftar_barang:
        print(f"- {barang}: Rp {harga}")
    print("Total harga keseluruhan: Rp", total)
    print("Terima kasih telah berbelanja di INDOMIE!\n")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lanjut.lower() != 'y':
        print("Kasir selesai.")
        break