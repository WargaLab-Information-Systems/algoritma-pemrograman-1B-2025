Inventaris = {}

def validasi_hanya_angka(teks):
    if not teks:
        return False
    return teks.isdigit()

def validasi_nama(teks):
    if not teks.strip():
        return False
    for char in teks:
        if not char.isalpha() and not char.isspace():
            return False
    return True

def validasi_id_barang(teks):

    if not teks.strip():
        return False
    
    for char in teks:
        if not (char.isalnum()): 
            return False
            
    return True

def validasi_harga(teks):
    if not teks or teks == '.':
        return False
    
    titik_desimal = 0
    
    for char in teks:
        if '0' <= char <= '9':
            continue
        elif char == '.':
            titik_desimal += 1
        else:
            return False
    
    if titik_desimal == 1 and (teks.startswith('.') or teks.endswith('.')):
        return False
        
    return titik_desimal <= 1 and bool(teks.strip())

def tampilkan_semua_barang():
    if not Inventaris:
        print("Inventaris kosong.")
    else:
        print("\n=== DAFTAR BARANG SAAT INI ===")
        barang_terurut = sorted(Inventaris.items())
        
        nomor = 1 
        for id_barang, info in barang_terurut:
            harga_format = f"{info[1]:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".") 
            print(f"{nomor}. ID: {id_barang}, Nama: {info[0]}, Harga: Rp{harga_format}, Stok: {info[2]}") 
            nomor += 1
    print()

def cari_barang():
    id_barang = input("Masukkan ID barang yang ingin dicari: ")
    if id_barang in Inventaris:
        info = Inventaris[id_barang]
        harga_format = f"{info[1]:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".")
        print(f"ID: {id_barang}, Nama: {info[0]}, Harga: Rp{harga_format}, Stok: {info[2]}")
    else:
        print(f"Barang dengan ID '{id_barang}' tidak ditemukan.")
    print()

def tambah_barang():
    while True:
        id_barang = input("Masukkan ID barang baru : ") 
        if validasi_id_barang(id_barang):
            break
        else:
            print("Input ID tidak valid. ID hanya boleh mengandung huruf dan/atau angka, dan tidak boleh kosong.")
            
    if id_barang in Inventaris:
        print("Barang dengan ID tersebut sudah ada.")
        print()
        return

    while True:
        nama = input("Masukkan nama barang (hanya huruf): ")
        if validasi_nama(nama):
            break
        else:
            print("Input nama tidak valid. Nama harus berupa huruf saja (spasi diizinkan).")

    while True:
        harga_input = input("Masukkan harga barang : ")
        if validasi_harga(harga_input):
            break
        else:
            print(" Input harga tidak valid. Harus berupa angka (desimal diizinkan).")

    while True:
        stok_input = input("Masukkan jumlah stok (angka bulat positif): ")
        if validasi_hanya_angka(stok_input):
            if int(stok_input) > 0: 
                break
            else:
                print("Stok harus lebih besar dari nol.")
        else:
            print(" Input stok tidak valid. Harus berupa angka bulat positif.")

    harga = float(harga_input)
    stok = int(stok_input)
    Inventaris[id_barang] = [nama, harga, stok]
    print(f"Barang '{nama}' berhasil ditambahkan.")
    print()

def perbarui_stok():
    tampilkan_semua_barang() 
    
    id_barang = input("Masukkan ID barang yang ingin diperbarui stoknya: ")
    if id_barang in Inventaris:
        nama_barang = Inventaris[id_barang][0]
        stok_lama = Inventaris[id_barang][2]
        
        print(f"Barang: {nama_barang}. Stok saat ini: {stok_lama}")
        
        while True:
            stok_input = input("Masukkan jumlah stok baru: ")
            if validasi_hanya_angka(stok_input) and int(stok_input) >= 0:
                break
            else:
                print("Input stok tidak valid. Harus berupa angka bulat positif atau nol.")
                
        stok_baru = int(stok_input)
        Inventaris[id_barang][2] = stok_baru
        print(f" Stok untuk barang '{nama_barang}' berhasil diperbarui dari {stok_lama} menjadi {stok_baru}.")
    else:
        print(f"Barang dengan ID '{id_barang}' tidak ditemukan.")
    print()

def hapus_barang():
    tampilkan_semua_barang()
    
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")
    if id_barang in Inventaris:
        info = Inventaris[id_barang]
        harga_format = f"{info[1]:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".")
        
        print("\n--- DETAIL BARANG YANG AKAN DIHAPUS ---")
        print(f"ID: {id_barang}, Nama: {info[0]}, Harga: Rp{harga_format}, Stok: {info[2]}")
        
        konfirmasi = input("Apakah Anda yakin ingin menghapus barang ini? (y/n): ").lower()
        
        if konfirmasi == 'y':
            del Inventaris[id_barang]
            print(f"Barang dengan ID '{id_barang}' berhasil dihapus.")
        else:
            print(f"Pembatalan. Barang dengan ID '{id_barang}' tidak jadi dihapus.")
    else:
        print(f"Barang dengan ID '{id_barang}' tidak ditemukan.")
    print()

def menu():
    while True:
        print("=== MENU INVENTARIS GUDANG ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan ID")
        print("3. Tambah barang baru")
        print("4. Perbarui stok barang")
        print("5. Hapus barang")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            tampilkan_semua_barang()
        elif pilihan == '2':
            cari_barang()
        elif pilihan == '3':
            tambah_barang()
        elif pilihan == '4':
            perbarui_stok()
        elif pilihan == '5':
            hapus_barang()
        elif pilihan == '6':
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid (masukkan angka 1-6). Silakan coba lagi.\n")

menu()
