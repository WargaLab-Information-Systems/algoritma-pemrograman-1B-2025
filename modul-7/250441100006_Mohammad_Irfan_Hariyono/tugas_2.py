def menu():
    print("\n Menu Inventaris ")
    print("1. Tambah barang ")
    print("2. Tampilkan semua barang ")
    print("3. Update Stok barang ")
    print("4. Hapus barang  ")
    print("5. Cari barang ")
    print("6. Keluar ")

def tambah_barang(daftar_barang):
    while True:
        id_barang = input("Masukkan ID barang seterah wkwk : ")
        if len(id_barang) == 0:
            print("Error: ID tidak boleh kosong (jangan req Enter aja)!")
            continue

        harus_angka = False
        for huruf in id_barang:
            if not huruf.isdigit():
                harus_angka = True
                break
        if harus_angka:
            print("ID harus berupa angka saja! (Tidak boleh ada huruf)")
            continue
        if id_barang in daftar_barang:
            print(f"Error : Barang dengan ID '{id_barang}' tersebut sudah ada ganti dengan ID lain")
            continue
        break
    while True:
        nama_barang = input("Masukkan nama barang : ")
        if len(nama_barang) == 0:
            print("Nama barang tidak boleh kosong")
            continue
        ada_angka = False
        for huruf in nama_barang:
            if huruf.isdigit():
                ada_angka = True
                break
        if ada_angka:
            print("Error nama barang tidak boleh angka / mengandung angka")
        else:
            break
    while True:
        harga_string = input("Masukkan harga Barang : ")

        if len(harga_string) == 0:
            print("Harga tidak boleh kosong")
            continue

        if not harga_string.isdigit():
            print("Error : Harga harus berupa angka (positif)!")
            continue
        harga_barang = int(harga_string)
        if harga_barang == 0:
            print("Error: Harga tidak boleh 0!")
            continue
        break
    while True:
        stok_string = input("Masukkan stok awal : ")

        if len(stok_string) == 0:
            print("Stok tidak boleh kosong!")
            continue
        stok_barang = int(stok_string)
        if stok_barang == 0:
            print("Error: Stok awal tidak boleh 0! (Minimal ada 1 barang dong)")
            continue
        break
    
    daftar_barang[id_barang] = [nama_barang, harga_barang, stok_barang]
    print(f"Barang '{nama_barang}' dengan ID: {id_barang} berhasil ditambahkan ")

def tampilkan(daftar_barang):
    if not daftar_barang:
        print(" Data inventaris gudang masih kosong ")
        return
    
    print(f"{'ID':<8} | {'Nama barang':<20} | {'Harga':<10} | {'Stok':<5}")
    print()

    for id_brg, info in daftar_barang.items():
        nama = info[0]
        harga = info[1]
        stok = info[2]
        print(f"{id_brg:<8} | {nama:<20} | {harga:<10} | {stok:<5}")

def update_stok(daftar_barang):
    id_barang = input("Masukkan ID barang yang stok nya ingin di update : ")

    if id_barang not in daftar_barang:
        print(f"Error : barang dengan ID {id_barang} tersebut tidak ditemukan ")
        return
    
    nama_barang = daftar_barang[id_barang][0]
    stok_barangg = daftar_barang[id_barang][2]
    print(f"Stok '{nama_barang}' saat ini adalah : {stok_barangg}")
    ubah_stok_str = input("Masukkan perubahan stok (contoh 5 utk menambah, -3 untuk mengurangi ) : ")
    if ubah_stok_str.isdigit():
        perubahan = int(ubah_stok_str)
    elif ubah_stok_str.startswith('-') and ubah_stok_str[1:].isdigit():
        perubahan = int(ubah_stok_str)
    else:
        print("Error: Perubahan stok harus berupa angka (cth: 5 atau -3).")
        return
    
    stok_baru = stok_barangg + perubahan
    
    if stok_baru < 0:
        print(f"Error: Gagal update. Stok tidak boleh menjadi negatif.")
        print(f"(Stok saat ini: {stok_barangg}, Perubahan: {perubahan}, Hasil akan: {stok_baru})")
    else:
        daftar_barang[id_barang][2] = stok_baru
        print(f"Stok '{nama_barang}' berhasil diupdate menjadi {stok_baru}.")

def hapus_barang(daftar_barang):
    id_barang = input("Masukkan ID Barang yang ingin dihapus: ")
    
    info_barang_dihapus = daftar_barang.pop(id_barang, None) 
    
    if info_barang_dihapus is not None:
        print(f"Barang '{info_barang_dihapus[0]}' (ID: {id_barang}) berhasil dihapus.")
    else:
        print(f"Error: Barang dengan ID '{id_barang}' tidak ditemukan.")

def cari_barang(daftar_barang):
    id_barang = input("Masukkan ID Barang yang ingin dicari: ")
    
    info_barang = daftar_barang.get(id_barang)
    
    if info_barang:
        print(f"\nDetail Barang (ID: {id_barang})")
        print(f"Nama  : {info_barang[0]}")
        print(f"Harga : {info_barang[1]}")
        print(f"Stok  : {info_barang[2]}")
    else:
        print(f"Error: Barang dengan ID '{id_barang}' tidak ditemukan.")

def inti():
    daftar_barang = {}

    while True:
        menu()
        pilih = input("Silakan pilih menu (1-6) : ")
        if pilih == "1":
            tambah_barang(daftar_barang)
        elif pilih == "2":
            tampilkan(daftar_barang)
        elif pilih == "3":
            update_stok(daftar_barang)
        elif pilih == "4":
            hapus_barang(daftar_barang)
        elif pilih == "5":
            cari_barang(daftar_barang)
        elif pilih == "6":
            print(" Keluar program Arigatou Ghozaimasu ")
            break
        else:
            print("Pilihan mu tidak ada di menu. Silakan pilih lagi (1-6)")

inti()