while True :  
    nama_pembeli = input("Masukkan nama pembeli: ")
    daftar_barang = []
    total_harga = 0

    while True:
        nama_barang = input("Nama barang: ")
        if nama_barang == "selesai":
            break
        harga_barang = int(input("Harga barang (Rp): "))
        daftar_barang += [(nama_barang, harga_barang)]
        total_harga += harga_barang

    print("=== Struk Pembelian Indomei ===")
    print("Nama Pembeli:", nama_pembeli)
    for barang, harga in daftar_barang:
        print(barang + " = Rp " + str(harga))
        
    print("Total Harga Barang =", total_harga)
    print("Terima kasih telah berbelanja di IndoMei.")

    berikutnya = input("Apakah lanjut ke pembeli berikutnya? (ya/tidak): ").lower()
    if berikutnya == "tidak":
        print("Terima kasih! Sampai ketemu lagi di IndoMei!")
        break