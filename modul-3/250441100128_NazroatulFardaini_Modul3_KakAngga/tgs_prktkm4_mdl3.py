# perulangan untuk setiap pembeli
while True:
    print("====IndoMei====")
    nama = input("masukkan nama pembeli: ") # input nama pembeli
    total_harga = 0
    daftar_barang = " "
    while True: # perulangan untuk input barang
        barang = input("masukkan nama barang: ")
        harga_barang = int(input("masukkan harga barang: "))
        total_harga += harga_barang
        # menambahkan ke daftar barang
        daftar_barang = daftar_barang + barang + "Rp" + str(harga_barang) + " "
        tambah_barang = input("apakah ingin menambahkan barang lagi? (y/n): ")
        if tambah_barang == "n":
           break
        elif tambah_barang != "y":
           print("input yang anda masukkan salah.mohon memasukan (y/n)")
           tambah_barang = input("apakah ingin menambahkan barang lagi? (y/n): ")
           
        
# tampilan struk pembelian
    print("STRUK PEMBELIAN")
    print("nama pembeli: ", nama)
    print("---------")
    print(daftar_barang)
    print("---------")
    print("total harga: Rp", total_harga)
    print("terima kasih telah berbelanja di IndoMie")
    print("")
    lanjutkan_perulangan = True
    ada_pembeli_berikutnya = input("apakah ada pembeli berikutnya? (y/n): ")
    if ada_pembeli_berikutnya == "n":
     print("kasir selesai bekerja. program berhenti")
     break
    elif ada_pembeli_berikutnya != "y":
       print("input yang anda masukkan salah.mohon memasukan (y/n)")
       ada_pembeli_berikutnya = input("apakah ada pembeli berikutnya? (y/n): ")

       