def tambah_pengunjung(data_kunjungan, id_pengunjung):
    print("\n   Tambah Data Pengunjung   ")
    nama_pengunjung = input("Nama pengunjung : ")
    nama_santri = input("Santri yang dijenguk: ")
    
    while True:
        daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if daerah in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        print("Daerah harus Sumatra, Kalimantan, atau Jawa!")
    
    data_kunjungan.append([id_pengunjung, nama_pengunjung, nama_santri, daerah])
    print(f"Data berhasil ditambahkan dengan ID Antrian: {id_pengunjung}")
    id_pengunjung += 1
    return id_pengunjung


def tampilkan_pengunjung(data_kunjungan):
    print("\n    Daftar Pengunjung    ")
    
    if len(data_kunjungan) == 0:
        print("Belum ada data pengunjung.")
        return
    
    sumatra = []
    kalimantan = []
    jawa = []
    
    for data in data_kunjungan:
        if data[3] == "Sumatra":
            sumatra.append(data)
        elif data[3] == "Kalimantan":
            kalimantan.append(data)
        else:
            jawa.append(data)
    
    urutan = [("Sumatra", sumatra), ("Kalimantan", kalimantan), ("Jawa", jawa)]
    
    for daerah, daftar in urutan:
        if len(daftar) > 0:
            print(f"\nDaerah {daerah}:")
            for d in daftar:
                print(f"  ID: {d[0]}  Pengunjung: {d[1]}  Santri: {d[2]}")


def hapus_pengunjung(data_kunjungan):
    print("\n=== Hapus Data Pengunjung ===")
    
    if len(data_kunjungan) == 0:
        print("Belum ada data pengunjung.")
        return
    
    id_hapus = int(input("Masukkan ID antrian yang akan dihapus: "))
    
    for i in range(len(data_kunjungan)):
        if data_kunjungan[i][0] == id_hapus:
            data_kunjungan.pop(i)
            print("Data berhasil dihapus!")
            return
    
    print("ID tidak ditemukan!")

data_kunjungan = []
id_pengunjung = 1

while True:
    print("\n    SISTEM KUNJUNGAN SANTRI    ")
    print("1. Tambah Pengunjung")
    print("2. Tampilkan Daftar Pengunjung")
    print("3. Hapus Pengunjung")
    print("4. Keluar")
    
    pilih = input("Pilih menu (1-4): ")
    
    if pilih == "1":
        id_pengunjung = tambah_pengunjung(data_kunjungan, id_pengunjung)
    elif pilih == "2":
        tampilkan_pengunjung(data_kunjungan)
    elif pilih == "3":
        hapus_pengunjung(data_kunjungan)
    elif pilih == "4":
        print("Terima kasih berkunjunggg :D!")
        break
    else:
        print("Pilihan tidak valid!")
