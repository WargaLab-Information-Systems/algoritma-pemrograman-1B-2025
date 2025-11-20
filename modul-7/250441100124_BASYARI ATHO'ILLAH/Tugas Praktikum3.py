diskon = {
    "BASYARI22": 0.5,
    "FAHIRA44": 0.3,
    "KECE00" : 0.2,
    "PRABOWO":0.35
}

def read():
    if not diskon:
        print(">>> Daftar diskon Kosong. <<<\n")
        return
    print(">>> Daftar diskon <<<")
    print("_________________________________________")
    for i in diskon:
        print(f"Kode: {i} => Diskon: {diskon[i]*100}%")
    print("_________________________________________")

def transaksi():
    print(">>> Transaksi Belanja <<<")
    while True:
        harga_belanja = input("Masukkan total harga belanja: Rp. ")
        if not harga_belanja.isdigit():
            print("Harga belanja harus berupa angka.\n")
        else:
            harga_belanja = int(harga_belanja)
            break
    kode_diskon = input("Masukkan kode diskon: ")
    if kode_diskon in diskon:
        nilai_diskon = diskon[kode_diskon]
        potongan = harga_belanja * nilai_diskon
        total_bayar = harga_belanja - potongan
        diskon.pop(kode_diskon)
        print("__________________________________________")
        print(f"Diskon sebesar {nilai_diskon * 100}% berhasil diterapkan.")
        print(f"Total harga setelah diskon: Rp. {total_bayar}")
        print("__________________________________________")
    else:
        print("Kode diskon tidak valid atau sudah digunakan.\n")
        total_bayar = harga_belanja
        print(f"Total harga tanpa diskon: Rp. {total_bayar}\n")
        

while True:
    print("\n=== Program Validasi Kupon ===")   
    print("1. Tampilkan Semua Kupon")
    print("2. Transaksi")
    print("3. Keluar")
    pilih = input("Pilih menu: ")
    if pilih == "1":
        read()
    elif pilih == "2":
        transaksi()
    elif pilih == "3":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

