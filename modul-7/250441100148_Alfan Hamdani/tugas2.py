# Program Manajemen Inventaris Gudang dengan ID Otomatis

inventaris = []

def buat_id(indeks):
    return str(indeks + 1).zfill(3)

def tampilkan_semua():
    if not inventaris:
        print("\nTidak ada barang dalam inventaris.")
    else:
        print("\n=== Daftar Semua Barang ===")
        for i, barang in enumerate(inventaris):
            id_barang = buat_id(i)
            print(f"ID Barang : {id_barang}")
            print(f"Nama      : {barang['nama']}")
            print(f"Harga     : {barang['harga']}")
            print(f"Stok      : {barang['stok']}")
            print("-" * 35)

def cari_barang():
    id_barang = input("Masukkan ID barang yang ingin dicari (contoh: 002): ")
    try:
        indeks = int(id_barang) - 1
        if 0 <= indeks < len(inventaris):
            barang = inventaris[indeks]
            print("\n=== Barang Ditemukan ===")
            print(f"ID Barang : {id_barang}")
            print(f"Nama      : {barang['nama']}")
            print(f"Harga     : {barang['harga']}")
            print(f"Stok      : {barang['stok']}")
        else:
            print("Barang tidak ditemukan!")
    except:
        print("ID harus berupa angka 3 digit!")

def tambah_barang():
    nama = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga barang: "))
    stok = int(input("Masukkan jumlah stok: "))

    inventaris.append({
        "nama": nama,
        "harga": harga,
        "stok": stok
    })

    print("Barang berhasil ditambahkan!")

def perbarui_stok():
    print("\n=== DAFTAR BARANG ===")
    tampilkan_semua()  

    id_barang = input("Masukkan ID barang yang ingin diperbarui stoknya: ")

    try:
        indeks = int(id_barang) - 1

        if 0 <= indeks < len(inventaris):
            perubahan = int(input("Masukkan perubahan stok (+ menambah, - mengurangi): "))
            stok_baru = inventaris[indeks]["stok"] + perubahan

            if stok_baru < 0:
                print("Stok tidak boleh negatif! Perubahan dibatalkan.")
            else:
                inventaris[indeks]["stok"] = stok_baru
                print("Stok berhasil diperbarui!")
        else:
            print("Barang tidak ditemukan!")
    except:
        print("Input tidak valid! ID harus angka.")

def hapus_barang():
    print("\n=== DAFTAR BARANG ===")
    tampilkan_semua()  
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")
    try:
        indeks = int(id_barang) - 1

        if 0 <= indeks < len(inventaris):
            del inventaris[indeks]
            print("Barang berhasil dihapus!")
        else:
            print("Barang tidak ditemukan!")
    except:
        print("ID harus berupa angka!")

# Menu Utama
while True:
    print("""
=== MANAJEMEN INVENTARIS GUDANG ===
1. Tampilkan Semua Barang
2. Cari Barang Berdasarkan ID
3. Tambah Barang Baru
4. Perbarui Stok Barang
5. Hapus Barang
6. Keluar
""")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_semua()
    elif pilihan == "2":
        cari_barang()
    elif pilihan == "3":
        tambah_barang()
    elif pilihan == "4":
        perbarui_stok()
    elif pilihan == "5":
        hapus_barang()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")