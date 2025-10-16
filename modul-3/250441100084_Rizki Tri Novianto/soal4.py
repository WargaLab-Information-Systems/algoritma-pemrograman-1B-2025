ulang = "y"

while ulang == "y":
    print()
    print("=== STRUK PEMBELIAN IndoMEI ===")
    nama = input("Nama pembeli: ")

    total = 0
    daftar_struk = ""
    print("Masukkan daftar barang (ketik '-' untuk selesai):")
    print("Daftar belanja:")
    nomor = 1
    while True:
        print("Barang ke-", nomor)
        nama_barang = input("  Nama barang: ")
        if nama_barang == "-":
            break

        harga_input = input("  Harga barang: ")

        # validasi harga
        if harga_input == "":
            print("  Tolong masukkan harga dengan benar.")
            continue

        karakter_salah = False
        jumlah_karakter = 0
        for karakter in harga_input:
            jumlah_karakter += 1
            if karakter < "0" or karakter > "9":
                karakter_salah = True
                break

        if jumlah_karakter == 0 or karakter_salah == True:
            print("  Tolong masukkan harga dengan benar.")
            continue

        # Konversi karakter ke angka 
        harga = 0
        for karakter in harga_input:
            angka = 0
            digit = "0123456789"
            for d in digit:
                if d == karakter:
                    break
                angka += 1
            harga = harga * 10 + angka

        total += harga
        no_str = str(nomor)

        barang_str = nama_barang + "                   "
        barang_final = ""
        hitung = 0
        for huruf in barang_str:
            barang_final = barang_final + huruf
            hitung = hitung + 1
            if hitung == 18:
                break

        harga_str = "Rp" + str(harga)
        baris = no_str + "   " + barang_final + "   " + harga_str + "\n"
        daftar_struk += baris
        nomor = nomor + 1

    print()
    print("===== TOTAL BELANJAAN =====")
    print("Nama Pembeli : ", nama)
    print("----------------------------------------")
    print("No  Nama Barang           Harga")
    print("----------------------------------------")
    print(daftar_struk, end="")
    print("----------------------------------------")
    print("TOTAL HARGA   : Rp", str(total))
    print("Terima kasih telah berbelanja di IndoMEI.")
    print()

    ulang = input("Apakah ada pembeli berikutnya? (y/n): ")