# Program Sistem Kunjungan Santri

kunjungan = []

# Fungsi untuk menambah data pengunjung
def tambah_data():
    nama = input("Masukkan nama santri: ")
    daerah = input("Masukkan daerah (Sumatra/Kalimantan/Jawa): ")
    kunjungan.append((nama, daerah))
    print("Data berhasil ditambahkan!\n")

def tampilkan_data():
    if not kunjungan:
        print("Belum ada data kunjungan.\n")
    else:
        print("\nDaftar Kunjungan:")
        for i, (nama, daerah) in enumerate(kunjungan, start=1):
            print(f"{i}. {nama} - {daerah}")
        print()

# Fungsi untuk menghapus data berdasarkan nama
def hapus_data():
    nama = input("Masukkan nama santri yang ingin dihapus: ")
    for data in kunjungan:
        if data[0].lower() == nama.lower():
            kunjungan.remove(data)
            print("Data berhasil dihapus!\n")
            return
    print("Data tidak ditemukan!\n")

def tampilkan_berdasarkan_daerah():
    urutan = ["Sumatra", "Kalimantan", "Jawa"]
    print("\nDaftar kunjungan berdasarkan daerah:")
    for d in urutan:
        for nama, daerah in kunjungan:
            if daerah.lower() == d.lower():
                print(f"{nama} - {daerah}")
    print()

# Menu utama
while True:
    print("=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Data")
    print("2. Tampilkan Semua Data")
    print("3. Hapus Data")
    print("4. Tampilkan Berdasarkan Daerah")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        tampilkan_berdasarkan_daerah()
    elif pilihan == "5":
        print("program selesai")
        break
    else:
        print("Pilihan tidak valid!\n")
