# kupon = {
#     "DISC10": 10,
#     "DISC20": 20,
#     "HEMAT5": 5
# }

# while True:
#     print("\n=== SISTEM KUPON DISKON ===")
#     print("1. Tampilkan kupon yang tersedia")
#     print("2. Gunakan kupon")
#     print("3. Keluar")

#     pilih = input("Pilih menu: ")

#     # 1. Tampilkan kupon
#     if pilih == "1":
#         if not kupon:
#             print("Tidak ada kupon lagi.")
#         else:
#             for kode, diskon in kupon.items():
#                 print(f"{kode} - {diskon}%")

#     # 2. Gunakan kupon
#     elif pilih == "2":
#         kode = input("Masukkan kode kupon: ")
#         if kode in kupon:
#             total = float(input("Total belanja: "))
#             diskon = kupon[kode]
#             potongan = total * (diskon / 100)
#             bayar = total - potongan

#             print(f"Diskon {diskon}% = Potongan {potongan}")
#             print(f"Total bayar: {bayar}")

#             del kupon[kode]  # Hapus kupon setelah dipakai
#             print("Kupon berhasil digunakan!")
#         else:
#             print("Kupon tidak valid atau sudah dipakai.")

#     # 3. Keluar
#     elif pilih == "3":
#         break

# kupon = {}    

# def tampil_kupon():
#     if not kupon:
#         print("Tidak ada kupon.")
#     else:
#         for kode, diskon in kupon.items():
#             print(f"Kode: {kode}, Diskon: {diskon}%")

# def tambah_kupon():
#     kode = input("Kode kupon: ")
#     diskon = int(input("Diskon (%): "))
#     kupon[kode] = diskon
#     print("Kupon ditambah.")

# def hapus_kupon():
#     kode = input("Kode yang dihapus: ")
#     if kode in kupon:
#         del kupon[kode]
#         print("Kupon dihapus.")
#     else:
#         print("Kupon tidak ada.")

# def pakai_kupon():
#     kode = input("Kode kupon: ")
#     if kode in kupon:
#         total = float(input("Total belanja: "))
#         diskon = kupon[kode] / 100 * total
#         bayar = total - diskon
#         print("Diskon:", diskon)
#         print("Total bayar:", bayar)
#         del kupon[kode]   # setelah dipakai dihapus
#         print("Kupon telah digunakan dan dihapus.")
#     else:
#         print("Kupon tidak valid.")

# while True:
#     print("\n1.Tampil 2.Tambah 3.Hapus 4.Pakai Kupon 5.Keluar")
#     pilih = input("Pilih: ")

#     if pilih == "1": tampil_kupon()
#     elif pilih == "2": tambah_kupon()
#     elif pilih == "3": hapus_kupon()
#     elif pilih == "4": pakai_kupon()
#     elif pilih == "5": break
#     else: print("Pilihan salah.")

# Program Validasi Kupon Diskon

# kupon = {}

# def tampilkan_kupon():
#     if not kupon:
#         print("Belum ada kupon.\n")
#     else:
#         for kode, diskon in kupon.items():
#             print(f"Kode Kupon : {kode} | Diskon : {diskon}%")

# def tambah_kupon():
#     kode = input("Masukkan kode kupon: ")
#     diskon = int(input("Masukkan diskon (%): "))
#     kupon[kode] = diskon
#     print("Kupon berhasil ditambahkan!\n")

# def pakai_kupon():
#     kode = input("Masukkan kode kupon: ")
#     if kode in kupon:
#         total = int(input("Masukkan total belanja: "))
#         diskon = kupon[kode]
#         potongan = total * diskon / 100
#         total_bayar = total - potongan

#         print(f"Diskon: {diskon}%")
#         print(f"Total potongan: {potongan}")
#         print(f"Total bayar: {total_bayar}\n")

#         del kupon[kode]  # kupon hanya bisa dipakai sekali
#         print("Kupon telah digunakan dan dihapus dari sistem!\n")
#     else:
#         print("Kupon tidak ditemukan.\n")

# # Menu Utama
# while True:
#     print("\n=== SISTEM KUPON DISKON ===")
#     print("1. Tampilkan semua kupon")
#     print("2. Tambah kupon")
#     print("3. Gunakan kupon")
#     print("4. Keluar")

#     pilihan = input("Pilih menu: ")

#     if pilihan == "1":
#         tampilkan_kupon()
#     elif pilihan == "2":
#         tambah_kupon()
#     elif pilihan == "3":
#         pakai_kupon()
#     elif pilihan == "4":
#         break
#     else:
#         print("Pilihan tidak valid!\n")



kupon = {} 

def tampilkan_kupon():
    if not kupon:
        print("Belum ada kupon.\n")
    else:
        for kode, diskon in kupon.items():
            print(f"Kode Kupon : {kode} | Diskon : {diskon}%")

def tambah_kupon():
    kode = input("Masukkan kode kupon: ")
    diskon = int(input("Masukkan diskon (%): "))
    kupon[kode] = diskon
    print("Kupon berhasil ditambahkan!\n")

def proses_transaksi():
    item = input("Masukkan nama barang yang ingin dipesan: ")
    harga = int(input("masukkan harga barang: "))
    jumlah = int(input("masukkan jumlah barang: "))


    total_belanja = harga *jumlah
    kode = input("Masukkan kode kupon: ")
    print("Total belanja: ",total_belanja)

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
    print("2. Tambahkan kupon")
    print("3. Proses Transaksi (Gunakan Kupon)")
    print("4. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1": tampilkan_kupon()
    elif pilih == "2": tambah_kupon()
    elif pilih == "3": proses_transaksi()
    elif pilih == "4": break
    else: print("Pilihan tidak valid!")