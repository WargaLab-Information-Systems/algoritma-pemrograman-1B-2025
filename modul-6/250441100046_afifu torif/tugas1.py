# List utama untuk menyimpan data kunjungan
data_kunjungan = []
id_antrian = 1  # ID akan bertambah setiap ada pengunjung baru


# Fungsi Tambah Data
def tambah_data():
    global id_antrian
 
    jumlah = int(input("Masukkan jumlah pengunjung yang ingin ditambah: "))

    for i in range(jumlah):
        print(f"\n--- Input Data Pengunjung ke-{i+1} ---")
        nama_pengunjung = input("Masukkan nama pengunjung: ")
        nama_santri = input("Masukkan nama santri yang dijenguk: ")
        daerah = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()

        if daerah not in ["Sumatra", "Kalimantan", "Jawa"]:
            print("Daerah tidak valid! Harus: Sumatra, Kalimantan, atau Jawa.")
            continue  # lewati dan lanjut ke pengunjung berikutnya

        # Tambah ke list utama (ID, Pengunjung, Santri, Daerah)
        data_kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah])
        print(f"Data berhasil ditambahkan dengan ID Antrian: {id_antrian}")
        id_antrian += 1  # naikkan ID tiap kali menambah data

    print(f"\n {jumlah} data pengunjung berhasil diproses!")


# Fungsi Tampilkan Data
def tampilkan_data():
    if not data_kunjungan:
        print("Belum ada data kunjungan.")
    else:
        print("\n=== DAFTAR PENGUNJUNG ===")
        
        # Pengelompokkan berdasarkan urutan daerah
        urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
        for d in urutan_daerah:
            print(f"\n--- Pengunjung dari {d} ---")
            for data in data_kunjungan:
                if data[3] == d:
                    print(f"ID: {data[0]}, Pengunjung: {data[1]}, Santri: {data[2]}")


# Fungsi Hapus Data
def hapus_data():
    if not data_kunjungan:
        print("Data kosong, tidak ada yang bisa dihapus.")
    else:
        hapus_id = int(input("Masukkan ID Antrian yang akan dihapus: "))
        ditemukan = False
        
        for data in data_kunjungan:
            if data[0] == hapus_id:
                data_kunjungan.remove(data)
                print(f"Data dengan ID {hapus_id} berhasil dihapus.")
                ditemukan = True
                break
        
        if not ditemukan:
            print("ID tidak ditemukan!")


# Fungsi Keluar
def keluar_program():
    print("Program selesai. Terima kasih.")


# Program utama (bagian loop tetap sama)
while True:
    print("\n=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Data Pengunjung")
    print("2. Tampilkan Daftar Pengunjung")
    print("3. Hapus Data Pengunjung")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1/2/3/4): ")
    
    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        keluar_program()
        break
    else:
        print("Pilihan tidak valid, coba lagi.")