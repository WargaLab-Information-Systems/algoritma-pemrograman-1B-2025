data_kunjungan = []
id_antrian = 1

while True:
    print("=== MENU KUNJUNGAN SANTRI ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Keluar")

    pilih = input("Pilih menu (1-4): ")

    if pilih == "1":
        print("-- Tambah Data --")
        nama_pengunjung = input("Nama Pengunjung : ")
        nama_santri = input("Nama Santri     : ")
        daerah = input("Daerah (Sumatra/Kalimantan/Jawa): ").capitalize()

        if daerah in ["Sumatra", "Kalimantan", "Jawa"]:
            data_kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah])
            print(f"Data disimpan dengan ID {id_antrian}")
            id_antrian += 1
        else:
            print("Daerah tidak valid!")

    elif pilih == "2":
        print("-- Daftar Kunjungan --")
        if not data_kunjungan:
            print("Belum ada data.")
        else:
            for d in ["Sumatra", "Kalimantan", "Jawa"]:
                print(f"Pengunjung dari {d}:")
                kosong = True
                for data in data_kunjungan:
                    if data[3] == d:
                        print(f"ID:{data[0]} | {data[1]} → {data[2]}")
                        kosong = False
                if kosong:
                    print("Tidak ada data.")

    elif pilih == "3":
        if not data_kunjungan:
            print("Belum ada data untuk dihapus.")
        else:
            try:
                hapus = int(input("Masukkan ID yang ingin dihapus: "))
                for data in data_kunjungan:
                    if data[0] == hapus:
                        data_kunjungan.remove(data)
                        print("Data berhasil dihapus.")
                        break
                else:
                    print("ID tidak ditemukan.")
            except:
                print("Masukkan angka ID yang benar!")

    elif pilih == "4":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")