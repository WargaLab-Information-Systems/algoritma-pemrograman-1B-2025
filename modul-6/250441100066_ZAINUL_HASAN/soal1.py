data_kunjungan = []
id_antrian = 1

def tambah_pengunjung(id_antrian):
    print("\n=== TAMBAH PENGUNJUNG ===")
    nama = input("Nama pengunjung: ")
    santri = input("Nama santri yang dijenguk: ")
    daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
    
    data_kunjungan.append([id_antrian, nama, santri, daerah])
    print(f"Data ditambahkan dengan ID {id_antrian}")
    return id_antrian + 1  

def tampilkan_data():
    if not data_kunjungan:
        print("\nBelum ada data kunjungan.")
        return

    print("\n=== DAFTAR KUNJUNGAN ===")
    urutan = ["Sumatra", "Kalimantan", "Jawa"]
    for d in urutan:
        print(f"\nDaerah {d}:")
        for data in data_kunjungan:
            if data[3] == d:
                print(f"ID {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]}")

def hapus_data():
    if not data_kunjungan:
        print("\nBelum ada data untuk dihapus.")
        return

    try:
        hapus = int(input("Masukkan ID yang ingin dihapus: "))
        ketemu = False
        for data in data_kunjungan:
            if data[0] == hapus:
                data_kunjungan.remove(data)
                print("Data berhasil dihapus.")
                ketemu = True
                break
        if not ketemu:
            print("ID tidak ditemukan.")
    except ValueError:
        print("Input harus berupa angka!")

def menu():
    id_antrian = 1  
    while True:
        print("\n=== MENU KUNJUNGAN SANTRI ===")
        print("1. Tambah Pengunjung")
        print("2. Tampilkan Semua Data")
        print("3. Hapus Data")
        print("4. Keluar")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            id_antrian = tambah_pengunjung(id_antrian)  
        elif pilih == "2":
            tampilkan_data()
        elif pilih == "3":
            hapus_data()
        elif pilih == "4":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak ada, coba lagi.")

menu()
