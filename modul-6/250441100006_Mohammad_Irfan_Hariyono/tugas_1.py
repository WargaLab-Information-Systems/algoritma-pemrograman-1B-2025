def tambah_pengunjung(list_kunjungan_dari_main, id_terakhir_dari_main):
    
    print("\nTambah Data Pengunjung")
    nama_pengunjung = input("Nama Pengunjung: ")
    nama_santri = input("Nama Santri: ")
    
    while True:
        print("Daerah asal : Sumatra, Kalimantan, Jawa")
        daerah_asal = input("Masukkan Daerah Asal: ").lower()
        
        if daerah_asal in ["sumatra", "kalimantan", "jawa"]:
            break
        else:
            print(" Perhatikan ketikan mu dek")
            
    id_terakhir_dari_main += 1
    id_antrian_baru = id_terakhir_dari_main
    
    data_baru = [id_antrian_baru, nama_pengunjung, nama_santri, daerah_asal]
    
    list_kunjungan_dari_main.append(data_baru)
    
    print(f"\nBerhasil! Data pengunjung '{nama_pengunjung}' telah ditambahkan.")
    print(f"ID Antrian Anda adalah: {id_antrian_baru}")
    
    return id_antrian_baru

def tampilkan_pengunjung(list_kunjungan_dari_main):
    print("\n Daftar Seluruh Kunjungan Santri")
    
    if not list_kunjungan_dari_main:
        print("Belum ada data yang terdaftar.")
        return
        
    daftar_daerah = ["sumatra", "kalimantan", "jawa"]
    for daerah_target in daftar_daerah:
        print(f"\nDAERAH {daerah_target.upper()}")

        data_ditemukan_di_daerah_ini = False
        for data in list_kunjungan_dari_main:
            if data[3] == daerah_target:
                print(f"ID: {data[0]} | Nama: {data[1]} | Menjenguk: {data[2]}")
                data_ditemukan_di_daerah_ini = True
        if not data_ditemukan_di_daerah_ini:
            print(f" (Tidak ada pengunjung dari {daerah_target})")

def hapus_pengunjung(list_kunjungan_dari_main):
    
    print("\nHapus Data Pengunjung")
    if not list_kunjungan_dari_main:
        print("Belum ada data.")
        return

    id_input_str = input("Masukkan ID Antrian: ")
    input_valid = True
    if len(id_input_str) == 0:
        input_valid = False
    else:
        for karakter in id_input_str:
            if karakter not in "0123456789":
                input_valid = False
                break 
    if not input_valid:
        print("ID Antrian harus berupa angka positif.")
        return
        
    id_hapus = int(id_input_str)
    
    data_yang_akan_dihapus = None
    
    for data in list_kunjungan_dari_main:
        if data[0] == id_hapus:
            data_yang_akan_dihapus = data
            break
            
    if data_yang_akan_dihapus:
        list_kunjungan_dari_main.remove(data_yang_akan_dihapus)
        print(f"Data dengan ID Antrian {id_hapus} telah berhasil dihapus.")
    else:
        print(f"Data dengan ID Antrian {id_hapus} tidak ditemukan.")

def main():
    list_kunjungan_lokal = []
    id_terakhir_lokal = 0
    
    while True:
        print("\nSistem Antrian Kunjungan Santri")
        print("1. Tambah")
        print("2. Tampilkan")
        print("3. Hapus")
        print("4. Keluar")
        
        pilihan = input("pilih (1-4): ")
        
        if pilihan == '1':
            id_terakhir_lokal = tambah_pengunjung(list_kunjungan_lokal, id_terakhir_lokal)
            
        elif pilihan == '2':
            tampilkan_pengunjung(list_kunjungan_lokal)
            
        elif pilihan == '3':
            hapus_pengunjung(list_kunjungan_lokal)
            
        elif pilihan == '4':
            print("\nKamu sudah keluar program.")
            break 
        else:
            print("\nHarap masukkan angka 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()