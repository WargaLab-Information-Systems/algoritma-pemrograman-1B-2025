data_kunjungan = []
id_antrian = 1

def tambah_pengunjung(data_kunjungan, id_antrian):
    if pilihan == "1":
            while True :
                nama_pengunjung = input("Masukkan nama pengunjung: ")
                ada_angka = False
                for karakter in nama_pengunjung:
                    if karakter in "0123456789":
                        ada_angka = True
                        break
                if ada_angka:
                    print("Nama pengunjung tidak boleh mengandung angka. Silakan coba lagi")
                else:
                    break

            while True :
                nama_santri = input("Masukkan nama santri yang dijenguk: ")
                ada_angka = False
                for karakter in nama_santri:
                    if karakter in "0123456789":
                        ada_angka = True
                        break
                if ada_angka:
                    print("Nama santri tidak boleh mengandung angka. Silakan coba lagi")
                else:
                    break
            
            while True:
                daerah = input("Masukkan daerah asal pengunjung (Sumatra/Kalimantan/Jawa):").lower()
                if daerah in ["sumatra", "kalimantan", "jawa"]:
                    break
                else :
                    print("Daerah tidak valid. Silahkan coba lagi") 
            data_kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah])
            print(f"Data berhasil ditambahkan dengan ID antrian: {id_antrian}")
            id_antrian += 1
            return id_antrian

def tampilkan_pengunjung(data_kunjungan):
    if not data_kunjungan:
        print("Belum ada data pengunjung.")
        return

    print("=== DAFTAR PENGUNJUNG ===")
    urutan = ["Sumatra", "Kalimantan", "Jawa"]
    for daerah in urutan:
        for data in data_kunjungan:
            if data[3].lower() == daerah.lower():
                print(f"ID: {data[0]} | Nama Pengunjung: {data[1]} | Santri: {data[2]} | Asal: {data[3]}")
    print()

def hapus_pengunjung(data_kunjungan):
    try:
        hapus_id = int(input("Masukkan ID antrian yang akan dihapus: "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    for data in data_kunjungan:
        if data[0] == hapus_id:
            data_kunjungan.remove(data)
            print("Data berhasil dihapus!")
            return
    print("ID tidak ditemukan!")

# Menu utama
while True:
    print("=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Pengunjung")
    print("2. Tampilkan Semua Pengunjung")
    print("3. Hapus Pengunjung")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        id_antrian = tambah_pengunjung(data_kunjungan, id_antrian)
    elif pilihan == "2":
        tampilkan_pengunjung(data_kunjungan)
    elif pilihan == "3":
        hapus_pengunjung(data_kunjungan)
    elif pilihan == "4":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")

    