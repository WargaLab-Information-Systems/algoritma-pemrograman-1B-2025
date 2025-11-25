Kupon_diskon = {
    "HEMAT10": 10,
    "DISKON20": 20,
    "SALE30": 30,
    "HEMATLEBARAN": 15
}


def validasi_float_manual(teks):
    if not teks or teks == '.':
        return False
        
    titik_desimal = 0

    for char in teks:
        if '0' <= char <= '9':
            continue
        elif char == '.':
            titik_desimal += 1
        else:
            return False 
    
    if titik_desimal == 1 and (teks.startswith('.') or teks.endswith('.')):
        return False
        
    return titik_desimal <= 1 and bool(teks.strip())


def tampilkan_kupon():
    print("\n---  Kupon yang Tersedia ---")
    if not Kupon_diskon:
        print("Tidak ada kupon yang tersedia saat ini.")
    
    else:
        for kode, diskon in Kupon_diskon.items():
            print(f"- {kode}: Diskon {diskon}%")
    print("------------------------------")

def tambah_barang_transaksi():
    keranjang = []
    total_belanja_awal = 0.0

    print("\n--- Input Barang Belanja ---")
    while True:
        nama_barang = input("Masukkan Nama Barang (Kosongkan dan Enter untuk selesai): ").strip()
        
        if not nama_barang:
            break
            
        while True:
            harga_input = input(f"Masukkan Harga Satuan {nama_barang}: Rp")
            if validasi_float_manual(harga_input) and float(harga_input) > 0:
                harga_satuan = float(harga_input)
                break
            else:
                print(" Input harga tidak valid. Masukkan angka positif.")

        while True:
            kuantitas_input = input(f"Masukkan Kuantitas {nama_barang}: ")
            if kuantitas_input.isdigit() and int(kuantitas_input) > 0:
                kuantitas = int(kuantitas_input)
                break
            else:
                print(" Input kuantitas tidak valid. Masukkan bilangan bulat positif.")
        
        subtotal = harga_satuan * kuantitas
        keranjang.append((nama_barang, harga_satuan, kuantitas, subtotal))
        total_belanja_awal += subtotal
        print(f"-> {nama_barang} ditambahkan")
        print(f"-> Subtotal: Rp{subtotal:,.2f}")

    return keranjang, total_belanja_awal

def proses_transaksi():
    
    keranjang, total_belanja = tambah_barang_transaksi()
    
    if not keranjang:
        print("Tidak ada barang dalam keranjang. Transaksi dibatalkan.")
        print()
        return
        
    total_belanja_format = f"{total_belanja:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".")
    
    print(f"\nTotal Belanja Awal Anda: Rp{total_belanja_format}")
    
    kode_kupon = input("Masukkan kode kupon (Kosongkan jika tidak ada): ").upper()
    
    potongan = 0.0
    diskon_persen = 0
    kupon_digunakan = False

    if kode_kupon and kode_kupon in Kupon_diskon:
        diskon_persen = Kupon_diskon[kode_kupon]
        
        potongan = total_belanja * (diskon_persen / 100)
        total_bayar = total_belanja - potongan
        kupon_digunakan = True
        
        del Kupon_diskon[kode_kupon]
        
    else:
        total_bayar = total_belanja
    
    print("\n===============================")
    print("    DETAIL PEMBAYARAN & BARANG")
    print("===============================")
    
    print("\n-- Daftar Barang --")
    for nama, harga, qty, subtotal in keranjang:
        harga_satuan_format = f"{harga:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".")
        subtotal_format = f"{subtotal:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".")
        print(f"| {nama:<15} ({qty}x) @Rp{harga_satuan_format:<10} = Rp{subtotal_format}")

    print("\n-- Ringkasan Total --")
    print(f"Total Belanja Awal : Rp{total_belanja_format}")
    
    if kupon_digunakan:
        potongan_format = f"{potongan:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".")
        total_bayar_format = f"{total_bayar:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".")
        
        print(f"Kupon Diskon       : '{kode_kupon}' ({diskon_persen}%)")
        print(f"Potongan Harga     : - Rp{potongan_format}")
        print("-------------------------------")
        print(f"Total Bayar Akhir  : Rp{total_bayar_format}")
        print("-------------------------------")
        print(f"Kupon '{kode_kupon}' telah digunakan dan dihapus dari sistem.")
        
    else:
        if kode_kupon:
            print(f"Kupon '{kode_kupon}' tidak valid atau sudah tidak tersedia.")
        
        total_bayar_format = f"{total_bayar:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".")
        print(f"Total Bayar Akhir  : Rp{total_bayar_format} (Tanpa Diskon)")

    print("===============================")
    print()

def menu():
    while True:
        print("\n===  SISTEM KASIR ===")
        print("1. Tampilkan semua kupon tersedia")
        print("2. Proses transaksi (Gunakan kupon)")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            tampilkan_kupon()
        elif pilihan == '2':
            proses_transaksi()
        elif pilihan == '3':
            print("\nTerima kasih, program kasir selesai.")
            break
        else:
            print("Pilihan tidak valid (masukkan angka 1-3). Silakan coba lagi.")

menu()

