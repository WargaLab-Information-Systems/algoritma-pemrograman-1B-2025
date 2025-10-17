# perulangan untuk setiap pembeli
while True:
    print("IndoMei")
    nama = input("masukkan nama pembeli: ") 
    total_harga = 0
    daftar_barang = " "
    while True: # perulangan untuk input barang
        barang = input("masukkan nama barang: ")
        harga_barang = int(input("masukkan harga barang: "))
        total_harga += harga_barang
        # menambahkan ke daftar barang yg dibeli
        daftar_barang = daftar_barang + barang + "Rp" + str(harga_barang) + " "
        tambah_barang = input("Masukkan nama barang (atau selesai jika sudah selesai): ")
        if tambah_barang.lower() == "selesai":
            break
# tampilan struk pembelian
    print("STRUK PEMBELIAN")
    print("nama pembeli: ", nama)
    print("")
    print(daftar_barang)
    print("")
    print("total harga: Rp", total_harga)
    print("terima kasih telah berbelanja di IndoMie")
    print("")
    while True:
        lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
        if lanjut.lower() == 'y':
            break
        elif lanjut.lower() == 'n':
            exit()
        else:
            print("Input tidak valid. Silakan masukkan y atau n.")
            