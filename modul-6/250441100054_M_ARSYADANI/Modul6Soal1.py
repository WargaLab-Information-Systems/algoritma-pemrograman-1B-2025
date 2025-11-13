# Sistem Kunjungan Santri

kunjungan = []

def tambah_pengunjung():
    id_ = len(kunjungan)+1
    nama = input("Nama pengunjung: ").lower()
    santri = input("Nama santri yang dijenguk: ").lower()
    daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").lower()
    while daerah not in ['sumatra', 'kalimantan', 'jawa']:
        daerah = input("Daerah tidak valid. Masukkan Sumatra/Kalimantan/Jawa: ").lower()
    kunjungan.append([nama, santri, daerah, id_])
    print(f"Data ditambahkan dengan ID: {id_}")

def tampilkan_pengunjung():
    if not kunjungan:
        print("Tidak ada data kunjungan.")
        return
    kelompok = {'sumatra': [], 'kalimantan': [], 'jawa': []}
    for data in kunjungan:
        kelompok[data[2]].append(data)
    for daerah in ['sumatra', 'kalimantan', 'jawa']:
        if kelompok[daerah]:
            print(f"\nDaerah {daerah.title()}:")
            for data in kelompok[daerah]:
                print(f"ID: {data[3]}, Nama: {data[0].title()}, Santri: {data[1].title()}")

def hapus_pengunjung():
    id_hapus = int(input("Masukkan ID antrian yang akan dihapus: "))
    data_dihapus = False  # untuk cek apakah ID ditemukan
    for data in kunjungan:
        if data[3] == id_hapus:  # kalau ID cocok
            kunjungan.remove(data)  # hapus data itu
            data_dihapus = True
            print("Data berhasil dihapus.")
            break  # hentikan loop setelah dihapus
    
    if not data_dihapus:
        print("ID tidak ditemukan.")


while True:
    print("\nMenu:")
    print("1. Tambah pengunjung")
    print("2. Tampilkan daftar pengunjung")
    print("3. Hapus pengunjung")
    print("4. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == '1':
        tambah_pengunjung()
    elif pilihan == '2':
        tampilkan_pengunjung()
    elif pilihan == '3':
        hapus_pengunjung()
    elif pilihan == '4':
        break
    else:
        print("Pilihan tidak valid.")
