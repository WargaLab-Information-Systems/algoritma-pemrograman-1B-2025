inventaris_gudang = {}

def tambah_barang():
    """Fungsi untuk menambahkan barang baru (Buat)"""
    id_barang = input("Masukkan ID barang: ")
    if id_barang in inventaris_gudang:
        print("Barang dengan ID tersebut sudah ada!")
        return
    nama_barang = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga barang: "))
    stok = int(input("Masukkan stok barang: "))
    inventaris_gudang[id_barang] = [nama_barang, harga, stok]
    print("Barang berhasil ditambahkan!")

def lihat_barang():
    """Fungsi untuk menampilkan semua barang (Baca)"""
    if not inventaris_gudang:
        print("Tidak ada barang yang tersimpan.")
        return
    print("\nDaftar Barang:")
    for id_barang, detail in inventaris_gudang.items():
        print(f"ID: {id_barang}, Nama: {detail[0]}, Harga: {detail[1]}, Stok: {detail[2]}")

def cari_barang():
    """Fungsi untuk mencari barang berdasarkan ID (Baca spesifik)"""
    id_barang = input("Masukkan ID barang yang dicari: ")
    if id_barang in inventaris_gudang:
        detail = inventaris_gudang[id_barang]
        print(f"ID: {id_barang}, Nama: {detail[0]}, Harga: {detail[1]}, Stok: {detail[2]}")
    else:
        print("Barang tidak ditemukan!")

def perbarui_stok():
    """Fungsi untuk memperbarui stok barang (Perbarui)"""
    id_barang = input("Masukkan ID barang yang ingin diperbarui: ")
    if id_barang in inventaris_gudang:
        stok_baru = int(input("Masukkan stok baru: "))
        if stok_baru < 0:
            print("Stok tidak boleh negatif!")
            return
        inventaris_gudang[id_barang][2] = stok_baru
        print("Stok barang berhasil diperbarui!")
    else:
        print("Barang tidak ditemukan!")

def hapus_barang():
    """Fungsi untuk menghapus barang (Hapus)"""
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")
    if id_barang in inventaris_gudang:
        del inventaris_gudang[id_barang]
        print("Barang berhasil dihapus!")
    else:
        print("Barang tidak ditemukan!")

# Menu utama
while True:
    print("\n=== Menu Manajemen Inventaris Gudang ===")
    print("1. Tambah Barang Baru")
    print("2. Lihat Semua Barang")
    print("3. Cari Barang")
    print("4. Perbarui Stok Barang")
    print("5. Hapus Barang")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == '1':
        tambah_barang()
    elif pilihan == '2':
        lihat_barang()
    elif pilihan == '3':
        cari_barang()
    elif pilihan == '4':
        perbarui_stok()
    elif pilihan == '5':
        hapus_barang()
    elif pilihan == '6':
        print("Terima kasih telah menggunakan sistem manajemen inventaris gudang!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
