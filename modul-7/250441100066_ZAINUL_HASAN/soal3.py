kupon = {
    "HEMAT10": 10,
    "DISKON5": 5,
} 

def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon tersedia.")
        return
    for kode, diskon in kupon.items():
        print(f"{kode} : {diskon}%")

def proses_transaksi():
    total_belanja = int(input("Masukkan total belanja: "))
    kode = input("Masukkan kode kupon: ")

    if kode not in kupon:
        print("Kupon tidak valid atau sudah dipakai!")
        return

    diskon = kupon[kode]
    potongan = total_belanja * diskon / 100
    total_bayar = int(total_belanja - potongan)

    print(f"Diskon {diskon}% diterapkan.")
    print(f"Total Bayar Setelah Diskon: Rp{total_bayar}")

    del kupon[kode]  
    print("Kupon telah digunakan dan dihapus dari sistem.")

while True:
    print("\n=== SISTEM KUPON KASIR ===")
    print("1. Tampilkan Kupon")
    print("2. Proses Transaksi (Gunakan Kupon)")
    print("3. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1": tampilkan_kupon()
    elif pilih == "2": proses_transaksi()
    elif pilih == "3": break
    else: print("Pilihan tidak valid!")
