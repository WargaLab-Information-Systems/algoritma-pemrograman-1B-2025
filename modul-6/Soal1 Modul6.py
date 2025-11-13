# Program Sistem Kunjungan Santri

# List utama penyimpan data kunjungan
# Setiap data berupa [id_antrian, nama_pengunjung, nama_santri, daerah_asal]
data_kunjungan = []
id_counter = 1  # Untuk memberi id_antrian otomatis

def tambah_pengunjung():
    global id_counter
    input("Masukkan nama pengunjung: ")
    nama_santri = input("Masukkan nama santri yang dijenguk: ")
    daerah_asal = input("Masunama_pengunjungkkan daerah asal (Sumatra/Kalimantan/Jawa): ")

    # Membuat sublist data
    data = [id_counter, nama_pengunjung, nama_santri, daerah_asal]
    data_kunjungan.append(data)
    print(f"Data pengunjung dengan ID {id_counter} berhasil ditambahkan!\n")
    id_counter += 1

def tampilkan_data():
    if not data_kunjungan:
        print("Belum ada data pengunjung.\n")
        return
    
    print("\n=== DAFTAR PENGUNJUNG BERDASARKAN DAERAH ===")
    
    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
    for daerah in urutan_daerah:
        print(f"\n-- Pengunjung dari {daerah} --")
        ada_data = False
        for pengunjung in data_kunjungan:
            if pengunjung[3].lower() == daerah.lower():
                print(f"ID: {pengunjung[0]}, Nama: {pengunjung[1]}, Santri: {pengunjung[2]}")
                ada_data = True
        if not ada_data:
            print("Tidak ada pengunjung dari daerah ini.")
    print()

def hapus_pengunjung():
    if not data_kunjungan:
        print("Belum ada data yang bisa dihapus.\n")
        return
    
    try:
        id_hapus = int(input("Masukkan ID antrian yang ingin dihapus: "))
        index = -1
        
        # Cari indeks data yang akan dihapus
        for i in range(len(data_kunjungan)):
            if data_kunjungan[i][0] == id_hapus:
                index = i
                break
        
        if index != -1:
            del data_kunjungan[index]
            print(f"Data dengan ID {id_hapus} berhasil dihapus.\n")
        else:
            print("ID tidak ditemukan.\n")
    except ValueError:
        print("Input ID harus berupa angka!\n")

# Menu utama
while True:
    print("=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Pengunjung")
    print("2. Tampilkan Semua Data")
    print("3. Hapus Pengunjung")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        tambah_pengunjung()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        hapus_pengunjung()
    elif pilihan == "4":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.\n")