# Program Validasi Kupon Diskon

kupon = {
    "DISC10": 10,
    "HEMAT20": 20,
    "SALE30": 30
}

# Daftar Barang
barang = {
    "1": ["Pulpen", 3000],
    "2": ["Buku Tulis", 6000],
    "3": ["Penghapus", 2000],
    "4": ["Pensil", 2500],
    "5": ["Kotak Pensil", 15000]
}

def tampilkan_kupon():
    if not kupon:
        print("\nTidak ada kupon yang tersedia.")
    else:
        print("\n=== Daftar Kupon Tersedia ===")
        for kode, diskon in kupon.items():
            print(f"Kode: {kode} — Diskon: {diskon}%")

def tampilkan_barang():
    print("\n=== Daftar Barang ===")
    for kode, info in barang.items():
        print(f"{kode}. {info[0]} — Rp {info[1]}")

def pembelian_barang():
    total_belanja = 0

    while True:
        tampilkan_barang()

        pilih = input("Pilih barang (1-5) atau 0 untuk selesai: ")

        if pilih == "0":
            break

        if pilih not in barang:
            print("Pilihan tidak valid! Coba lagi.")
            continue

        try:
            jumlah = int(input("Masukkan jumlah: "))
        except ValueError:
            print("Jumlah harus berupa angka!")
            continue

        nama = barang[pilih][0]
        harga = barang[pilih][1]
        subtotal = harga * jumlah

        total_belanja += subtotal

        print(f"Ditambahkan: {nama} x{jumlah} = Rp {subtotal}")

    print(f"\nTotal belanja sebelum diskon: Rp {total_belanja}")
    return total_belanja

def proses_transaksi():
    total_belanja = pembelian_barang()

    if total_belanja == 0:
        print("Tidak ada barang yang dibeli.")
        return

    kode = input("Masukkan kode kupon (atau tekan Enter untuk tanpa kupon): ").upper()

    if kode == "":
        print(f"Total yang harus dibayar: Rp {total_belanja}")
        return

    if kode in kupon:
        diskon = kupon[kode]
        potongan = total_belanja * (diskon / 100)
        total_bayar = total_belanja - potongan

        print(f"\nKupon valid! Anda mendapatkan diskon {diskon}%.")
        print(f"Potongan: Rp {potongan}")
        print(f"Total bayar: Rp {total_bayar}")

        # Hapus kupon yang sudah dipakai
        del kupon[kode]
        print("Kupon telah digunakan dan dihapus dari sistem.")
    else:
        print("Kupon tidak valid atau sudah digunakan!")
        print(f"Total yang harus dibayar: Rp {total_belanja}")

# Menu Utama
while True:
    print("""
=== SISTEM KASIR — VALIDASI KUPON DISKON ===
1. Tampilkan Semua Kupon
2. Proses Pembelian & Transaksi
3. Keluar
""")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        tampilkan_kupon()
    elif pilihan == "2":
        proses_transaksi()
    elif pilihan == "3":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")