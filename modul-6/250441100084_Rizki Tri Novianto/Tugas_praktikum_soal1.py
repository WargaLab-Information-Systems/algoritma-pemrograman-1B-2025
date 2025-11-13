data_kunjungan = []
id_antrian = 1

def tambah_kunjungan(data_kunjungan, id_antrian):
    print("\n=== Tambah Data Kunjungan ===")
    nama_pengunjung = input("Nama pengunjung: ")
    nama_santri = input("Nama santri yang dijenguk: ")
    daerah_asal = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").lower()

    if daerah_asal in ["sumatra", "kalimantan", "jawa"]:
        data_kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah_asal])
        print("Data berhasil ditambahkan.")
        return id_antrian + 1
    else:
        print("Daerah tidak valid! Hanya boleh: Sumatra, Kalimantan, atau Jawa.")
        return id_antrian

def tampilkan_kunjungan(data_kunjungan):
    print("\n=== Daftar Kunjungan Santri ===")
    urutan_daerah = ["sumatra", "kalimantan", "jawa"]
    ada_data = False

    for daerah in urutan_daerah:
        daftar_daerah = [k for k in data_kunjungan if k[3] == daerah]#membuat list baru dari variabel daerah
        if daftar_daerah:
            print(f"\n--- Pengunjung dari {daerah.capitalize()} ---")
            for data in daftar_daerah:
                print(f"ID {data[0]}: Pengunjung ({data[1]}) | Santri ({data[2]})")
            ada_data = True

    if not ada_data:
        print("Belum ada data kunjungan.")

def hapus_kunjungan(data_kunjungan):
    print("\n=== Hapus Data Kunjungan ===")
    try:#perintah yang digunakan untuk menangani error jika input bukan angka
        id_hapus = int(input("Masukkan ID antrian yang ingin dihapus: "))
        for i in range(len(data_kunjungan)):
            if data_kunjungan[i][0] == id_hapus:#cek apakah id yang dimasukkan ada di data_kunjungan
                del data_kunjungan[i]
                print("Data berhasil dihapus.")
                return
        print("ID tidak ditemukan.")
    except ValueError:#menangkap error jika input bukan angka
        print("Input harus berupa angka.")

def menu():
    data_kunjungan = []
    id_antrian = 1
    while True:
        print("\n=== Sistem Kunjungan Santri ===")
        print("1. Tambah Kunjungan")
        print("2. Tampilkan Daftar Kunjungan")
        print("3. Hapus Kunjungan")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")
        if pilihan == "1":
            id_antrian = tambah_kunjungan(data_kunjungan, id_antrian)
        elif pilihan == "2":
            tampilkan_kunjungan(data_kunjungan)
        elif pilihan == "3":
            hapus_kunjungan(data_kunjungan)
        elif pilihan == "4":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()
