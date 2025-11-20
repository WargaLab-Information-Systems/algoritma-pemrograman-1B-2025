inventaris = {}

def create():
    print(">>> Tambah Barang Baru <<<")
    while True:
        id_barang = input("Masukkan ID barang: ")
        if not id_barang.isdigit():
            print("ID barang harus berupa angka.")
        elif id_barang in inventaris:
            print("Barang dengan ID tersebut sudah ada!")
        else:
            break
    nama_barang = input("Masukkan nama barang: ")
    while True:
        harga = input("Masukkan harga barang: ")
        if not harga.isdigit():
            print("Harga barang harus berupa angka.")
        else:
            break
    while True:
        stok = input("Masukkan stok barang: ")
        if not stok.isdigit():
            print("Stok barang harus berupa angka.")
        else:
            break
    inventaris[id_barang] = [nama_barang, harga, stok]
    print(f"Barang berhasil ditambahkan dengan id {id_barang}\n")

def read():
    if not inventaris:
        print(">>> Daftar Inventaris Kosong. <<<\n")
        return 
    print("=== Daftar Inventaris Barang ===")
    print("________________________________\n")
    for id_barang in inventaris:
        print(f"| ID     : {id_barang}")
        print(f"| Nama   : {inventaris[id_barang][0]}")
        print(f"| Harga  : Rp. {inventaris[id_barang][1]}")
        print(f"| Stok   : {inventaris[id_barang][2]}")
        print("________________________________")

def cari():
    print(">>> Cari Barang <<<")
    id_barang = input("Masukkan ID barang: ")
    if id_barang in inventaris:
        print("--- Barang ditemukan ---")
        print("________________________________")
        print(f"| ID     : {id_barang}")
        print(f"| Nama   : {inventaris[id_barang][0]}")
        print(f"| Harga  : Rp. {inventaris[id_barang][1]}")
        print(f"| Stok   : {inventaris[id_barang][2]}\n")
        print("________________________________")
    else:
        print("Barang Tidak Ditemukan.\n")

def update():
    print(">>> Update Stok Barang <<<")
    id_barang = input("Masukkan ID barang yang ingin diperbarui stoknya: ")
    
    if id_barang in inventaris:
        print(f"Stok lama: {inventaris[id_barang][2]}")
        while True:
            stok_baru = input("Masukkan stok baru: ")
            if not stok_baru.isdigit():
                print("Stok barang harus berupa angka.")
            else:
                break
        stok_lama = inventaris[id_barang][2]
        total_stok = int(stok_lama) + int(stok_baru)
        inventaris[id_barang][2] = total_stok
        print("Stok berhasil diperbarui!\n")
    else:   
        print("Barang tidak ditemukan.\n")

def delete():
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")
    if id_barang in inventaris:
        del inventaris[id_barang]
        print("Barang berhasil dihapus!\n")
    else:
        print("Barang tidak ditemukan.\n")

while True:
    print("\n--- MENU INVENTARIS BARANG ---")
    print("1. Tambah Barang")
    print("2. Tampilkan Semua Barang")
    print("3. Cari Barang")
    print("4. Update Stok Barang")
    print("5. Hapus Barang")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        create()
    elif pilihan == "2":
        read()
    elif pilihan == "3":
        cari()
    elif pilihan == "4":
        update()
    elif pilihan == "5":
        delete()
    elif pilihan == "6":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")