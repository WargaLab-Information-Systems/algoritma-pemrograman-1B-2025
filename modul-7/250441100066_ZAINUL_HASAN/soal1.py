contacts = {}  

def tampilkan_kontak():
    if not contacts:
        print("Tidak ada kontak.")
        return
    for nama, info in contacts.items():
        print(f"Nama : {nama}")
        print(f"Telepon : {info['telp']}")
        print(f"Email : {info['email']}")
        print("-" * 30)

def cari_kontak():
    nama = input("Masukkan nama yang dicari: ")
    if nama in contacts:
        print("Kontak ditemukan!")
        print(f"Telepon: {contacts[nama]['telp']}")
        print(f"Email  : {contacts[nama]['email']}")
    else:
        print("Kontak tidak ditemukan.")

def tambah_kontak():
    nama = input("Nama: ")
    telp = input("Nomor Telepon: ")
    email = input("Email: ")
    contacts[nama] = {"telp": telp, "email": email}
    print("Kontak berhasil ditambahkan!")

def update_kontak():
    nama = input("Masukkan nama kontak yang ingin diperbarui: ")
    if nama not in contacts:
        print("Kontak tidak ditemukan.")
        return
    telp = input("Nomor Telepon baru: ")
    email = input("Email baru: ")
    contacts[nama] = {"telp": telp, "email": email}
    print("Kontak berhasil diperbarui!")

def hapus_kontak():
    nama = input("Masukkan nama yang ingin dihapus: ")
    if nama not in contacts:
        print("Kontak tidak ditemukan.")
        return
    del contacts[nama]
    print("Kontak berhasil dihapus.")

while True:
    print("\n=== CONTACT BOOK ===")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak")
    print("4. Update Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tampilkan_kontak()
    elif pilih == "2":
        cari_kontak()
    elif pilih == "3":
        tambah_kontak()
    elif pilih == "4":
        update_kontak()
    elif pilih == "5":
        hapus_kontak()
    elif pilih == "6":
        break
    else:
        print("Pilihan tidak valid!")
