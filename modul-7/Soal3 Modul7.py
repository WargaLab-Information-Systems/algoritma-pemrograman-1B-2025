# Program Validasi Kupon Diskon

kupon = {}

def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon yang tersedia.\n")
        return
    print("Daftar Kupon Tersedia:")
    for kode, diskon in kupon.items():
        print(f"- {kode}: {diskon}%")
    print()
    
def tambah_kupon():
    kode = input("Kode kupon baru: ")
    if kode in kupon:
        print("Kode kupon sudah ada.\n")
        return
    diskon = int(input("Masukkan persentase diskon: "))
    kupon[kode] = diskon
    print("Kupon berhasil ditambahkan.\n")

def proses_transaksi():
    total = float(input("Total belanja: "))
    kode = input("Masukkan kode kupon: ")

    if kode not in kupon:
        print("Kupon tidak valid atau sudah dipakai.\n")
        return

    diskon = kupon[kode]
    total_setelah_diskon = total - (total * diskon / 100)

    print(f"Diskon: {diskon}%")
    print(f"Total yang harus dibayar: {total_setelah_diskon}\n")

    del kupon[kode]   # kupon dihapus setelah dipakai
    print("Kupon telah digunakan dan dihapus.\n")

def menu_kupon():
    while True:
        print("=== MENU KUPON DISKON ===")
        print("1. Tampilkan Kupon")
        print("2. Tambah Kupon")
        print("3. Proses Transaksi")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == "1":
            tampilkan_kupon()
        elif pilihan == "2":
            tambah_kupon()
        elif pilihan == "3":
            proses_transaksi()
        elif pilihan == "4":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.\n")

# Menjalankan Program
menu_kupon()