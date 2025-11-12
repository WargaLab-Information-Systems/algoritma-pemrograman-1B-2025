data_pengunjung = []
id_kunjungan = 1

def create_pengunjung():
    global id_kunjungan
    print("=== Tambah Pengunjung ===")
    nama_pengunjung = input("Masukkan nama pengunjung: ")
    nama_santri = input("Masukkan nama santri: ")
    while True:
        asal_daerah = input("Masukkan asal daerah(jawa/sumatra/kalimantan): ").lower()
        if asal_daerah in ["jawa", "sumatra", "kalimantan"]:
            break
        else:
            print("Asal daerah tidak valid. Silakan masukkan lagi.")
    data_pengunjung.append([id_kunjungan, nama_pengunjung, nama_santri, asal_daerah])
    print(f"Pengunjung {nama_pengunjung} dengan ID {id_kunjungan} berhasil ditambahkan.")
    id_kunjungan += 1

def read_pengunjung():
    if not data_pengunjung:
        print("\nTidak ada data pengunjung.")
        return
 
    print("\n=== Daftar Kunjungan Santri ===")

    urutan_daerah = ["sumatra", "kalimantan", "jawa"]
    for daerah in urutan_daerah:
        print(f"\n Daerah {daerah}:")
        for kunjungan in data_pengunjung:
            if kunjungan[3] == daerah:
                print(f"ID {kunjungan[0]} | Pengunjung: {kunjungan[1]} | Santri: {kunjungan[2]}")

def delete_pengunjung():
    if not data_pengunjung:
        print("\n Tidak ada data untuk dihapus.")
        return

    try:
        id_hapus = int(input("\nMasukkan ID antrian yang ingin dihapus: "))
        for kunjungan in data_pengunjung:
            if kunjungan[0] == id_hapus:
                data_pengunjung.remove(kunjungan)
                print(f"Data dengan ID {id_hapus} berhasil dihapus.")
                return
        print("ID tidak ditemukan.")
    except ValueError:
        print("Input harus berupa angka.")


while True:
    print("\n=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Data Pengunjung")
    print("2. Tampilkan Semua Data")
    print("3. Hapus Data Pengunjung")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        create_pengunjung()
    elif pilihan == "2":
        read_pengunjung()
    elif pilihan == "3":
        delete_pengunjung()
    elif pilihan == "4":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
