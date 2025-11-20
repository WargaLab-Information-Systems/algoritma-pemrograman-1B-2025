inventaris = {} 

def tampilkan_barang():
    if not inventaris:
        print("Tidak ada barang.")
        return
    for id, barang in inventaris.items():
        print(f"ID      : {id}")
        print(f"Nama    : {barang['nama']}")
        print(f"Harga   : {barang['harga']}")
        print(f"Stok    : {barang['stok']}")
        print("-" * 30)

def cari_barang():
    id = input("Masukkan ID barang: ")
    if id not in inventaris:
        print("Barang tidak ditemukan.")
        return
    b = inventaris[id]
    print(f"Nama: {b['nama']}, Harga: {b['harga']}, Stok: {b['stok']}")

def tambah_barang():
    id = input("ID Barang: ")
    nama = input("Nama Barang: ")
    harga = int(input("Harga: "))
    stok = int(input("Stok: "))
    inventaris[id] = {"nama": nama, "harga": harga, "stok": stok}
    print("Barang berhasil ditambahkan!")

def update_barang():
    id = input("ID barang yang ingin diperbarui: ")
    if id not in inventaris:
        print("Barang tidak ditemukan.")
        return
    nama = input("Nama Baru: ")
    harga = int(input("Harga Baru: "))
    stok = int(input("Stok Baru: "))
    inventaris[id] = {"nama": nama, "harga": harga, "stok": stok}
    print("Data barang berhasil diperbarui!")

def tambah_stok():
    id = input("Masukkan ID: ")
    if id not in inventaris:
        print("Barang tidak ditemukan.")
        return
    jumlah = int(input("Jumlah stok yang ditambahkan: "))
    inventaris[id]["stok"] += jumlah
    print("Stok berhasil ditambah!")

def kurangi_stok():
    id = input("Masukkan ID: ")
    if id not in inventaris:
        print("Barang tidak ditemukan.")
        return
    jumlah = int(input("Jumlah yang diambil: "))
    if jumlah > inventaris[id]["stok"]:
        print("Stok tidak cukup!")
        return
    inventaris[id]["stok"] -= jumlah
    print("Stok berhasil dikurangi!")

def hapus_barang():
    id = input("Masukkan ID yang ingin dihapus: ")
    if id not in inventaris:
        print("Barang tidak ditemukan.")
        return
    del inventaris[id]
    print("Barang berhasil dihapus!")

while True:
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Lihat Semua Barang")
    print("2. Cari Barang")
    print("3. Tambah Barang")
    print("4. Update Barang")
    print("5. Tambah Stok")
    print("6. Kurangi Stok")
    print("7. Hapus Barang")
    print("8. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1": tampilkan_barang()
    elif pilih == "2": cari_barang()
    elif pilih == "3": tambah_barang()
    elif pilih == "4": update_barang()
    elif pilih == "5": tambah_stok()
    elif pilih == "6": kurangi_stok()
    elif pilih == "7": hapus_barang()
    elif pilih == "8": break
    else: print("Pilihan tidak valid!")
