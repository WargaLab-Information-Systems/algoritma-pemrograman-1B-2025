# Program Inventaris Gudang 
inventaris = {}

def tampilkan_barang():
    if not inventaris:
        print("Belum ada barang dalam inventaris.\n")
        return
    print("Daftar Inventaris:")
    for id_brg, data in inventaris.items():
        print(f"- ID {id_brg}: Nama = {data[0]}, Harga = {data[1]}, Stok = {data[2]}")
    print()

def cari_barang():
    id_brg = input("Masukkan ID barang yang dicari: ")
    if id_brg in inventaris:
        nama, harga, stok = inventaris[id_brg]
        print(f"Nama: {nama}, Harga: {harga}, Stok: {stok}\n")
    else:
        print("Barang tidak ditemukan.\n")

def tambah_barang():
    id_brg = input("ID Barang baru: ")
    if id_brg in inventaris:
        print("ID sudah digunakan.\n")
        return
    
    nama = input("Nama barang: ")
    harga = int(input("Harga barang: "))
    stok = int(input("Stok barang: "))
    
    inventaris[id_brg] = [nama, harga, stok]
    print("Barang berhasil ditambahkan.\n")

def update_stok():
    id_brg = input("Masukkan ID barang yang ingin diubah stoknya: ")
    if id_brg not in inventaris:
        print("Barang tidak ditemukan.\n")
        return

    stok_baru = int(input("Masukkan stok baru: "))
    if stok_baru < 0:
        print("Stok tidak boleh negatif.\n")
        return
    
    inventaris[id_brg][2] = stok_baru
    print("Stok berhasil diperbarui.\n")

def hapus_barang():
    id_brg = input("Masukkan ID barang yang ingin dihapus: ")
    if id_brg not in inventaris:
        print("Barang tidak ditemukan.\n")
        return

    del inventaris[id_brg]
    print("Barang berhasil dihapus.\n")

def menu_inventaris():
    while True:
        print("=== MENU INVENTARIS GUDANG ===")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang")
        print("3. Tambah Barang")
        print("4. Update Stok Barang")
        print("5. Hapus Barang")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            cari_barang()
        elif pilihan == "3":
            tambah_barang()
        elif pilihan == "4":
            update_stok()
        elif pilihan == "5":
            hapus_barang()
        elif pilihan == "6":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.\n")

# MENJALANKAN PROGRAM
menu_inventaris()