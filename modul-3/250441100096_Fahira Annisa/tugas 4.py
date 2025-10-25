while True:
    print("== Program Struk Pembelian Indomei ==")
    
    nama_pembeli = input("Masukkan nama pembeli: ")
    jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
    total = 0
    daftar_barang = " "

    for i in range(jumlah_barang):
        nama_barang = input(f"Nama barang : ")
        harga = int(input(f"Masukkan harga {nama_barang}: "))
        total += harga
        daftar_barang += f"{nama_barang} - Rp{harga}"
    
    print("="*15 )
    print("total harga: Rp", total)
    print("Terima kasih telah berbelanja di IndoMei.")
    print("="*20 )

    # jika y maka while tetep lanjut
    lanjut = input("Apakah lanjut ke pembeli berikutnya? (iya/ tidak): ").lower()
    if lanjut == "tidak":
        print("Program selesai. Sampai jumpa!")
        break