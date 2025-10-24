while True:
    nama_pembeli = input("Masukkan nama pembeli: ")

    total_harga = 0

    print("              Warung IndoMei              ")
    print(f"Nama Pembeli: {nama_pembeli}")
    print("==========================================")

    while True:
        nama_barang = input("Masukkan nama barang: ")

        while True:
            harga_input = input(f"Masukkan harga untuk {nama_barang}: Rp ")

            if harga_input == "":
                print("Input tidak valid! Harga harus berupa angka.")
            else:
                semua_angka = True
                for karakter in harga_input:
                    angka = False
                    if karakter == "0123456789":
                        angka = True

                    if angka == False:
                        semua_angka == False
                        break
                
                if semua_angka == True:
                    harga_barang = int(harga_input)
                    total_harga = total_harga + harga_barang
                    break
                else:
                    print("Input tidak valid! Harga harus berupa angka.")

        print(f"{nama_barang} Rp {harga_barang}")

        tambah_barang = input("Tambah barang lagi? (ya/tidak): ")
        if tambah_barang != "ya":
            break
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"{"TOTAL"} Rp {total_harga}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("   Terima kasih telah berbelanja di IndoMei   ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    pembeli_baru = input("Apakah ada pembeli berikutnya? (ya/tidak): ")
    if pembeli_baru != "ya":
        print("cetak struk selesai")
        break