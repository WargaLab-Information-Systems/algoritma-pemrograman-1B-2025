lanjut = 'ya'

while lanjut == 'ya':
    nama = input("siapa nama anda: ")

    total = 0
    daftar = ""  # Menyimpan baris pada struk
    nomor = 1
    print("==Meja Kasir IndoMei==")
    print("Masukkan daftar barang (ketik stop untuk selesai):")

    while True:  
        print("Barang ke-", nomor)
        nama_barang = input("  Nama barang: ")
        if nama_barang == "stop":
            break
        harga = int(input("  Harga barang: "))
        total += harga

        no = str(nomor)

        barang = nama_barang 
        final = ""
        hitung = 0
        for huruf in barang:
            final = final + huruf
            hitung = hitung + 1
            if hitung == 18:
                break

        hb = "Rp" + str(harga)

        baris = no + "  " + final + "   " + hb + "\n"
        daftar += baris

        nomor = nomor + 1

    print()
    print("STRUK PEMBELIAN")
    print("Nama Pembeli : " , nama)
    print("daftar belanjaan")
    print(daftar, end="")
    print("TOTAL HARGA   : Rp" , str(total))
    print("Terima kasih telah berbelanja di IndoMEI.")
    print()
    
    lanjut = input("Apakah ada pembeli berikutnya?: ")
    if lanjut == 'tidak':
        break  