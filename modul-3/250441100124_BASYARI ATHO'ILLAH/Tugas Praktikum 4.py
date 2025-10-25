while True:
    print("\n===  Struk Pembelian Indomei ===")
    print("="*15)
    nama_pembeli = input("Masukkan nama pembeli: ")
    daftar_barang = " "
    total_harga = 0
    print("=" * 15)
    while True:
        nama_barang = input("Nama barang: ")
        if nama_barang == "0":
            break
        
        harga_barang = int(input("Harga barang (Rp): "))
        total_harga += harga_barang
        
        daftar_barang += f"{nama_barang} = {harga_barang}"

    print("="* 15)
    
    print(f"Total Harga Barang = Rp {total_harga}")
    print("Terima kasih telah berbelanja di IndoMei.")
    print("="*15 )

    # jika y maka while tetep lanjut
    lanjut = input("Apakah lanjut ke pembeli berikutnya? (y/n): ").lower()
    if lanjut != "y":
        print("Program selesai. Sampai jumpa!")
        break

# a = [b, c]
# print(a)