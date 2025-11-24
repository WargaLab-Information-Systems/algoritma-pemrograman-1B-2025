kupon_diskon = {
    'POTONGAN10': 10,
    'HEMAT20': 20,
    'PENAWARAN15': 15,
    'BONUS5': 5
}

def tampilkan_kupon():
    """Menampilkan semua kupon yang masih tersedia."""
    if kupon_diskon:
        print("\nKupon yang tersedia:")
        for kode, persentase in kupon_diskon.items():
            print(f"- {kode}: {persentase}% diskon")
    else:
        print("\nTidak ada kupon yang tersedia.")

def proses_transaksi():
    """Memproses transaksi dengan kupon."""
    nama_barang = input("Masukkan nama barang: ")
    if not nama_barang.strip():
        print("\nNama barang tidak boleh kosong!")
        return
    
    harga_barang_input = input(f"Masukkan harga {nama_barang}: ")
    if not harga_barang_input.isdigit():
        print("\nInput tidak valid. Pastikan harga barang adalah angka.")
        return
    harga_barang = float(harga_barang_input)
    
    print(f"\n--- Detail Pembelian ---")
    print(f"Barang: {nama_barang}")
    print(f"Harga: Rp{harga_barang:,.0f}")
    print("------------------------")
    
    kode_kupon = input("Masukkan kode kupon: ")

    if kode_kupon == "":
        print(f"\nTotal yang harus dibayar: Rp{harga_barang:,.0f}")
        print("Transaksi berhasil tanpa kupon diskon.")
    elif kode_kupon in kupon_diskon:
        persentase = kupon_diskon[kode_kupon]
        diskon = harga_barang * (persentase / 100)
        total_bayar = harga_barang - diskon
        
        print(f"\nKupon valid! Diskon {persentase}%: Rp{diskon:,.0f}")
        print(f"Total yang harus dibayar: Rp{total_bayar:,.0f}")
        print(f"Anda hemat: Rp{diskon:,.0f}")

        del kupon_diskon[kode_kupon]
        print("Kupon telah digunakan dan dihapus.")
    else:
        print("\nKupon tidak valid atau sudah digunakan.")
        print(f"Total yang harus dibayar: Rp{harga_barang:,.0f}")

def menu():
    """Menu utama program."""
    while True:
        print("\n=== Sistem Kasir - Validasi Kupon Diskon ===")
        print("1. Tampilkan kupon tersedia")
        print("2. Proses transaksi")
        print("3. Keluar")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            tampilkan_kupon()
        elif pilihan == '2':
            proses_transaksi()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem kasir.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-3.")

menu()
