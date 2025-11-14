# Program Sistem Kunjungan Santri
def tampilkan_menu():
    print("\n=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Data Kunjungan")
    print("2. Tampilkan Daftar Kunjungan")
    print("3. Hapus Data Kunjungan")
    print("4. Keluar")

def tambah_kunjungan(daftar_kunjungan, id_antrian):
    print("\n--- Tambah Data Kunjungan ---")
    while True:
        nama_pengunjung = input("Masukkan nama pengunjung: ")
        if nama_pengunjung.replace(' ', '').isalpha():
            break
        else:
            print("Nama pengunjung harus berupa karakter huruf!")
    
    while True:
        nama_santri = input("Masukkan nama santri yang dijenguk: ")
        if nama_santri.replace(' ', '').isalpha():
            break
        else:
            print("Nama santri harus berupa karakter huruf!")
    
    while True:
        daerah = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if daerah in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        else:
            print("Daerah asal tidak valid! Harus Sumatra, Kalimantan, atau Jawa.")
    
    data = [id_antrian, nama_pengunjung, nama_santri, daerah]
    daftar_kunjungan.append(data)
    print(f"Data berhasil ditambahkan dengan ID Antrian: {id_antrian}")
    return id_antrian + 1  

def tampilkan_kunjungan(daftar_kunjungan):
    print("\n--- Daftar Kunjungan Santri ---")
    if not daftar_kunjungan:
        print("Belum ada data kunjungan.")
        return
    
    
    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
    for daerah in urutan_daerah:
        print(f"\nDaerah: {daerah}")
        for data in daftar_kunjungan:
            if data[3] == daerah:
                print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]} | Asal: {data[3]}")

def hapus_kunjungan(daftar_kunjungan):
    print("\n--- Hapus Data Kunjungan ---")
    id_hapus = input("Masukkan ID Antrian yang ingin dihapus: ")
    for data in daftar_kunjungan:
        if str(data[0]) == id_hapus:
            daftar_kunjungan.remove(data)
            print("Data berhasil dihapus.")
            return
    print("Data dengan ID tersebut tidak ditemukan.")

# --- Program Utama ---
daftar_kunjungan = []
id_antrian = 1
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-4): ")
    if pilihan == "1":
        id_antrian = tambah_kunjungan(daftar_kunjungan, id_antrian)
    elif pilihan == "2":
        tampilkan_kunjungan(daftar_kunjungan)
    elif pilihan == "3":
        hapus_kunjungan(daftar_kunjungan)
    elif pilihan == "4":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
