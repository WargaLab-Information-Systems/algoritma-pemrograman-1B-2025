kupon_master = {
    "HEMAT10": 10,
    "DISKON25": 25,
    "SUPERBIG50": 50,
    "AYOBELANJA": 15
}

kupon_tersedia = kupon_master.copy() 


def menu():
    print("   Program Validasi Kupon Diskon")
    print("1. Tampilkan Kupon Tersedia")
    print("2. Proses Transaksi")
    print("3. Keluar")

def tampilkan(kupon):

    if not kupon:
        print("Saat ini tidak ada kupon yang tersedia.")
    else:
        print("Kode Kupon   | Persentase Diskon")
        print()
        for kode, diskon in kupon.items():
            print(f"{kode:<12} | {diskon}%")
    print()

def transaksi(kupon_aktif, master_list):
    
    total_belanja = 0
    keranjang = []
    while True:
        print()
        nama_barang = input("Masukkan nama barang : ")
        while True:
            harga_input = input(f"Masukkan harga '{nama_barang}': Rp")
            if harga_input.isdigit():
                harga = int(harga_input)
                total_belanja += harga

                keranjang.append([nama_barang, harga])
                break
            else:
                print("Error Harga harus angka jangan pakai titik/koma")

        tanya = input("Tambah barang lagi tidak? : (y/n)")
        if tanya == "n":
            break
    print("       STRUK BELANJA")
    for item in keranjang:
        print(f"{item[0]:<20} : Rp{item[1]}")
    print(f"TOTAL TAGIHAN        : Rp{total_belanja}")
        
    kode_kupon = input("Masukkan kode kupon (jika ada): ").upper()

    if kode_kupon in kupon_aktif:
        print(f"\nKupon '{kode_kupon}' ditemukan!")

        diskon_persen = kupon_aktif[kode_kupon]
        potongan = (diskon_persen / 100) * total_belanja
        total = total_belanja - potongan

        diskon_fix = int(potongan)
        total_bayar = int(total)

        print(f"Anda mendapatkan diskon {diskon_persen}%")
        print(f"Total Belanja     : Rp{total_belanja}")
        print(f"Potongan diskon   : Rp{diskon_fix}")
        print(f"Total yang dibayar: Rp{total_bayar}")

        kupon_aktif.pop(kode_kupon)
        print(f"\n(Info: Kupon '{kode_kupon}' telah digunakan dan dihapus.)")
    elif kode_kupon == "":
        print("Tidak ada kupon yang dimasukkan")
        print(f"Total yang dibayar  : Rp{total_belanja}")
        print()
                
    elif kode_kupon in master_list:
        print(f"\nKupon '{kode_kupon}' SUDAH DIGUNAKAN dan tidak berlaku lagi.")
        print(f"Total yang dibayar: Rp{total_belanja}")

    else:
        print(f"\nKode kupon '{kode_kupon}' TIDAK VALID.")
        print(f"Total yang dibayar: Rp{total_belanja}")


def main():
    while True:
        menu()
        pilihan = input("Masukkan pilihan Anda (1/2/3): ")
        
        if pilihan == '1':
            tampilkan(kupon_tersedia)
            
        elif pilihan == '2':
            transaksi(kupon_tersedia, kupon_master)
            
        elif pilihan == '3':
            print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
            break
            
        else:
            print("\nPilihan tidak valid. Silakan masukkan 1, 2, atau 3.")

main()