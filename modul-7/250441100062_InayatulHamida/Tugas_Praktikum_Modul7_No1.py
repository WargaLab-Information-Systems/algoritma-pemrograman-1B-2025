def tambah_kontak(kontak, nama, nomor, email):
    if nama in kontak:
        print("Kontak sudah ada.")
    else:
        kontak[nama] = [nomor, email]
        print("Kontak berhasil ditambahkan.")

def cari_kontak(kontak, nama):
    if nama in kontak:
        info = kontak[nama]
        print(f"Kontak Ditemukan - Nama: {nama}, No Telepon: {info[0]}, Email: {info[1]}")
    else:
        print("Kontak tidak ditemukan.")

def tampilkan_kontak(kontak):
    if not kontak:
        print("Tidak ada kontak yang tersedia.")
    else:
        for nama, info in kontak.items():
            print(f"Nama: {nama}, No Telepon: {info[0]}, Email: {info[1]}")

def perbarui_email(kontak, nama, email_baru):
    if nama in kontak:
        kontak[nama][1] = email_baru
        print("Email kontak berhasil diperbarui.")
    else:
        print("Kontak tidak ditemukan.")

def hapus_kontak(kontak, nama):
    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")

def menu(kontak):
    while True:
        print("\nMenu Kontak:")
        print("1. Tambah kontak")
        print("2. Cari Kontak")
        print("3. Tampilkan kontak")
        print("4. Perbarui Email Kontak")
        print("5. Hapus Kontak")
        print("6. Keluar")

        pilihan = input("Pilih opsi (1-6): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama kontak: ")
            nomor = input("Masukkan nomor telepon: ")
            email = input("Masukkan email: ")
            tambah_kontak(kontak, nama, nomor, email)
        elif pilihan == '2':
            nama = input("Masukkan nama yang dicari: ")
            cari_kontak(kontak, nama)
        elif pilihan == '3':
            tampilkan_kontak(kontak)
        elif pilihan == '4':
            nama = input("Masukkan nama kontak yang ingin diperbarui: ")
            email_baru = input("Masukkan email baru: ")
            perbarui_email(kontak, nama, email_baru)
        elif pilihan == '5':
            nama = input("Masukkan nama kontak yang ingin dihapus: ")
            hapus_kontak(kontak, nama)
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    kontak = {}
    menu(kontak)