# Program Contact Book dengan CRUD
# Kontak disimpan sebagai list agar memiliki nomor urut rapi

contacts = []

def tampilkan_semua():
    if not contacts:
        print("\nTidak ada kontak yang tersimpan.")
    else:
        print("\n=== Daftar Semua Kontak ===")
        for i, c in enumerate(contacts, start=1):
            print(f"No : {i}")
            print(f"Nama : {c['nama']}")
            print(f"Telepon : {c['telepon']}")
            print(f"Email : {c['email']}")
            print("-" * 30)

def cari_kontak():
    nama = input("Masukkan nama kontak yang ingin dicari: ")
    for c in contacts:
        if c["nama"].lower() == nama.lower():
            print("\n=== Kontak Ditemukan ===")
            print(f"Nama : {c['nama']}")
            print(f"Telepon : {c['telepon']}")
            print(f"Email : {c['email']}")
            return
    print("Kontak tidak ditemukan!")

def tambah_kontak():
    nama = input("Masukkan nama: ")
    if not nama.isalpha():
        print("Nama tidak boleh mengandung angka!")
        return
    
    for c in contacts:
        if c["nama"].lower() == nama.lower():
            print("Nama sudah ada dalam kontak!")
            return

    telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")

    if "@gmail" not in email:
        print("Email tidak valid! Email harus mengandung '@gmail'.")
        return

    contacts.append({"nama": nama, "telepon": telepon, "email": email})
    print("Kontak berhasil ditambahkan!")

def perbarui_email():
    tampilkan_semua()
    try:
        no = int(input("Masukkan nomor kontak yang emailnya ingin diperbarui: "))
        if no < 1 or no > len(contacts):
            print("Nomor kontak tidak valid!")
            return
    except ValueError:
        print("Harus memasukkan angka!")
        return

    email_baru = input("Masukkan email baru: ")
    if "@gmail" not in email_baru:
        print("Email tidak valid! Email harus mengandung '@gmail'.")
        return

    contacts[no - 1]["email"] = email_baru
    print("Email berhasil diperbarui!")

def hapus_kontak():
    tampilkan_semua()
    try:
        no = int(input("Masukkan nomor kontak yang ingin dihapus: "))
        if no < 1 or no > len(contacts):
            print("Nomor kontak tidak valid!")
            return
    except ValueError:
        print("Harus memasukkan angka!")
        return

    del contacts[no - 1]
    print("Kontak berhasil dihapus!")

# Menu Utama
while True:
    print("""
=== CONTACT BOOK ===
1. Tampilkan Semua Kontak
2. Cari Kontak
3. Tambah Kontak Baru
4. Perbarui Email Kontak
5. Hapus Kontak
6. Keluar
""")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_semua()
    elif pilihan == "2":
        cari_kontak()
    elif pilihan == "3":
        tambah_kontak()
    elif pilihan == "4":
        perbarui_email()
    elif pilihan == "5":
        hapus_kontak()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")