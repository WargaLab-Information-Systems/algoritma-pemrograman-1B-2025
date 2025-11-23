#Nomer 3
kupon = {           
    "disc10": 10,
    "disc20": 20,
    "hemat5": 5
}

while True:
    print()
    print("=== SISTEM KUPON DISKON ===")
    print("1. Tampilkan semua kupon")
    print("2. Proses transaksi")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    
    if pilihan == "1": 
        kosong = True
        for k in kupon:
            kosong = False
            break

        if kosong:
            print("Tidak ada kupon tersedia.")
        else:
            print()
            print("=== DAFTAR KUPON ===")
            for k in kupon:
                print(f"Kode: {k} | Diskon: {kupon[k]}%")           

    
    elif pilihan == "2": 
        while True:
            total = input("Masukkan total belanja: ")

            angka_valid = True
            for angka in total:        
                if angka not in "0123456789":
                    angka_valid = False
                    break

            if angka_valid:
                total = float(total)
                break
            else:
                print("Input tidak valid! Total belanja harus angka atau jangan negatif dan jangan gunakan simbol")

        kode = input("Masukkan kode kupon: ")

        
        if kode in kupon:
            diskon = kupon[kode]
            potongan = total * diskon / 100
            total_bayar = total - potongan

            print("\nKupon valid!")
            print("Diskon :", diskon, "%")
            print("Total setelah diskon :", total_bayar)

            del kupon[kode]   
        else:
            print("Kode kupon tidak valid atau sudah digunakan.")

   
    elif pilihan == "3":
        print("Program selesai.")
        break

    
    else:
        print("Pilihan tidak valid.")
