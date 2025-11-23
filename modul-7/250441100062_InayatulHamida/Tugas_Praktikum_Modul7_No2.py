def tambah_barang(inventaris, id_barang, nama, harga, stok):
    if id_barang in inventaris:
        print("Barang sudah ada, gunakan ID yang berbeda.")
    else:
        inventaris[id_barang] = [nama, harga, stok]
        print("Barang berhasil ditambahkan.")
        
def cari_barang(inventaris, id_barang):
    if id_barang in inventaris:
        info = inventaris[id_barang]
        print(f"Barang Ditemukan - ID: {id_barang}, Nama Barang: {info[0]}, Harga: {info[1]}, Stok: {info[2]}")
    else:
        print("Barang tidak ditemukan.")

def tampilkan_barang(inventaris):
    if not inventaris:
        print("Tidak ada barang yang tersedia.")
    else:
        print("Daftar barang dalam inventaris:")
        for id_barang, info in inventaris.items():
            print(f"ID: {id_barang}, Nama Barang: {info[0]}, Harga: {info[1]}, Stok: {info[2]}")

def perbarui_stok(inventaris, id_barang, stok_baru):
    if id_barang in inventaris:
        if stok_baru < 0:
            print("Stok tidak boleh negatif.")
        else:
            inventaris[id_barang][2] = stok_baru
            print("Stok barang berhasil diperbarui.")
    else:
        print("Barang tidak ditemukan.")

def hapus_barang(inventaris, id_barang):
    if id_barang in inventaris:
        del inventaris[id_barang]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

def menu(inventaris):
    while True:
        print("\nMenu Inventaris:")
        print("1. Tambah barang")
        print("2. Cari Barang")
        print("3. Tampilkan semua Barang")
        print("4. Perbarui Stok Barang")
        print("5. Hapus Barang")
        print("6. Keluar")

        pilihan = input("Pilih opsi (1-6): ")
        
        if pilihan == '1':
            id_barang = input("Masukkan ID barang: ")
            nama = input("Masukkan nama barang: ")
            try:
                harga = float(input("Masukkan harga barang: "))
                stok = int(input("Masukkan stok barang: "))
                tambah_barang(inventaris, id_barang, nama, harga, stok)
            except ValueError:
                print("Input tidak valid! Pastikan harga adalah angka dan stok adalah bilangan bulat.")
        elif pilihan == '2':
            id_barang = input("Masukkan ID barang yang dicari: ")
            cari_barang(inventaris, id_barang)
        elif pilihan == '3':
            tampilkan_barang(inventaris)
        elif pilihan == '4':
            id_barang = input("Masukkan ID barang yang ingin diperbarui: ")
            try:
                stok_baru = int(input("Masukkan stok baru: "))
                perbarui_stok(inventaris, id_barang, stok_baru)
            except ValueError:
                print("Input tidak valid! Pastikan stok baru adalah bilangan bulat.")
        elif pilihan == '5':
            id_barang = input("Masukkan ID barang yang ingin dihapus: ")
            hapus_barang(inventaris, id_barang)
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    inventaris = {}
    menu(inventaris)