# Program Contact Book dengan CRUD

contacts = {}

def tampilkan_kontak():
    if not contacts:
        print("Belum ada kontak yang tersimpan.\n")
        return
    print("Daftar Kontak:")
    for nama, info in contacts.items():
        print(f"- {nama}: Telepon = {info[0]}, Email = {info[1]}")
    print()

def cari_kontak():
    nama = input("Masukkan nama yang ingin dicari: ")
    if nama in contacts:
        print(f"Ditemukan! Telepon: {contacts[nama][0]}, Email: {contacts[nama][1]}\n")
    else:
        print("Kontak tidak ditemukan.\n")

def tambah_kontak():
    nama = input("Nama kontak baru: ")
    if nama in contacts:
        print("Nama sudah ada, gunakan nama lain.\n")
        return
    telp = input("Nomor telepon: ")
    email = input("Email: ")
    contacts[nama] = [telp, email]
    print("Kontak berhasil ditambahkan.\n")

def update_email():
    nama = input("Nama kontak yang ingin diperbarui emailnya: ")
    if nama not in contacts:
        print("Kontak tidak ditemukan.\n")
        return
    email_baru = input("Email baru: ")
    contacts[nama][1] = email_baru
    print("Email berhasil diperbarui.\n")

def hapus_kontak():
    nama = input("Nama kontak yang ingin dihapus: ")
    if nama not in contacts:
        print("Kontak tidak ditemukan.\n")
        return
    del contacts[nama]
    print("Kontak berhasil dihapus.\n")

def menu_contact_book():
    while True:
        print("=== MENU CONTACT BOOK ===")
        print("1. Tampilkan Semua Kontak")
        print("2. Cari Kontak")
        print("3. Tambah Kontak")
        print("4. Update Email Kontak")
        print("5. Hapus Kontak")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")
        print()

        if pilihan == "1":
            tampilkan_kontak()
        elif pilihan == "2":
            cari_kontak()
        elif pilihan == "3":
            tambah_kontak()
        elif pilihan == "4":
            update_email()
        elif pilihan == "5":
            hapus_kontak()
        elif pilihan == "6":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.\n")

# PENTING! Jalankan fungsi ini agar program tampil:
menu_contact_book()