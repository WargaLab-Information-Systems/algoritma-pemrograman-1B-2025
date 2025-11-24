data_kontak = {}

def tambah_kontak():
    """Fungsi untuk menambahkan kontak baru (Buat)"""
    nama = input("Masukkan nama kontak: ")
    if nama in data_kontak:
        print("Kontak dengan nama tersebut sudah ada!")
        return
    telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")
    data_kontak[nama] = [telepon, email]
    print("Kontak berhasil ditambahkan!")

def lihat_kontak():
    """Fungsi untuk menampilkan semua kontak (Baca)"""
    if not data_kontak:
        print("Tidak ada kontak yang tersimpan.")
        return
    print("\nDaftar Kontak:")
    for nama, detail in data_kontak.items():
        print(f"Nama: {nama}, Telepon: {detail[0]}, email: {detail[1]}")

def cari_kontak():
    """Fungsi untuk mencari kontak berdasarkan nama (Baca spesifik)"""
    nama = input("Masukkan nama kontak yang dicari: ")
    if nama in data_kontak:
        detail = data_kontak[nama]
        print(f"Nama: {nama}, Telepon: {detail[0]}, email: {detail[1]}")
    else:
        print("Kontak tidak ditemukan!")

def perbarui_kontak():
    """Fungsi untuk memperbarui email kontak (Perbarui)"""
    nama = input("Masukkan nama kontak yang ingin diperbarui: ")
    if nama in data_kontak:
        email_baru = input("Masukkan email baru: ")
        data_kontak[nama][1] = email_baru
        print("email kontak berhasil diperbarui!")
    else:
        print("Kontak tidak ditemukan!")

def hapus_kontak():
    """Fungsi untuk menghapus kontak (Hapus)"""
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    if nama in data_kontak:
        del data_kontak[nama]
        print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan!")

# Menu utama
while True:
    print("\n=== Menu Buku Kontak ===")
    print("1. Tambah Kontak Baru")
    print("2. Lihat Semua Kontak")
    print("3. Cari Kontak")
    print("4. Perbarui email Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == '1':
        tambah_kontak()
    elif pilihan == '2':
        lihat_kontak()
    elif pilihan == '3':
        cari_kontak()
    elif pilihan == '4':
        perbarui_kontak()
    elif pilihan == '5':
        hapus_kontak()
    elif pilihan == '6':
        print("Terima kasih telah menggunakan Buku Kontak!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
