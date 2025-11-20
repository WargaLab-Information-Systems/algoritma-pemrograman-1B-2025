kupon = {
    "DISKON10": 10,
    "DISKON20": 20,
    "DISKON30": 30, 
    "DISKON50": 50,
    "DISKONMEMBER": 15
}

def tampilkan():
    print("Kupon yang tersedia:")
    for kode, diskon in kupon.items():
        print(f"Kode: {kode}, Diskon: {diskon}%")
        
def transaksi():
    while True:
        belanja = input("Apakah Anda ingin melakukan transaksi? (ya/tidak): ")
        if belanja == 'tidak' or belanja == 'Tidak':
            print("Terima kasih telah berkunjung.")
            break
        Kupon = input("apakah anda memiliki kupon? (ya/tidak): ")
        total_belanjaan = 0
        stuk = []
        if Kupon == 'Tidak' or Kupon == 'tidak':
            while True:
                namabelanjaan = input("Masukkan barang belanjaan: ")
                if namabelanjaan == "-":
                    break
                hargabelanjaan = float(input("Masukkan harga barang: "))
                total_belanjaan += hargabelanjaan 
                stuk.append(f"{namabelanjaan}: Rp.{hargabelanjaan}")
            print("\n--- Struk Pembayaran ---")
            for item in stuk:
                print(item)
            print(f"Total yang harus dibayar: Rp {total_belanjaan:.2f}")
            break
        else:
            while True:
                namabelanjaan = input("Masukkan barang belanjaan: ")
                if namabelanjaan == "-":
                    print()
                    break
                hargabelanjaan = float(input("Masukkan harga barang: "))
                total_belanjaan += hargabelanjaan
                stuk.append(f"{namabelanjaan}: Rp.{hargabelanjaan}")

            kodekupon = input("Masukkan kode kupon: ")
            if kodekupon in kupon:
                diskon = kupon[kodekupon]
                totaldiskon = total_belanjaan * (diskon / 100)
                totalsemua = total_belanjaan - totaldiskon
                print(f"Kupon tersedia")
                print(f"Anda mendapatkan diskon {diskon}%. Total yang harus dibayar: Rp {totalsemua:.2f}")
                del kupon[kodekupon]
                print(f"Kupon '{kodekupon}' telah digunakan")

                print("\n--- Struk Pembayaran ---")
                for item in stuk:
                    print(item)
                print(f"Total belanjaan: Rp {total_belanjaan:.2f}")
                print(f"Diskon: Rp {totaldiskon:.2f}")
                print(f"Total yang harus dibayar: Rp {totalsemua:.2f}")
                break
        
def menu():
    while True:
        print("\nmenu Validasi Kupon Diskon:")
        print("1. Tampilkan semua kupon yang tersedia")
        print("2. Proses transaksi")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == '1':
            tampilkan()
        elif pilihan == '2':
            transaksi()
        elif pilihan == '3':
            print("program selesai")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
            
menu()
