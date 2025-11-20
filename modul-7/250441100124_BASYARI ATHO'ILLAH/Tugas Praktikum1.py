kontak = {}

def create():
    print(">>> Tambah Kontak Baru <<<")
    nama = input("Masukkan nama kontak: ").lower()
    if nama in kontak:
        print("Nama kontak sudah ada.")
        return
    
    while True:
        telepon = input("Masukkan nomor telepon: ")
        if not telepon.isdigit():
            print("Nomor telepon harus berupa angka.")
        elif telepon in [kontak[n][0] for n in kontak]:
            print("Nomor telepon sudah ada.")
        else:
            break

    while True:
        email = input("Masukkan email: ").lower()
        if "@" not in email:
            print("Email tidak valid.")
        elif email in [kontak[n][1] for n in kontak]:
            print("Email sudah ada.")
        else:
            break
        
    kontak[nama] = [telepon, email]
    print("Kontak berhasil ditambahkan!\n")

def read():
    if not kontak:
        print(">>> Daftar Kontak Kosong. <<<\n")
        return
    print("=== Daftar Kontak ===")
    for nama in kontak:
        print(f"Nama: {nama}")
        print(f"Telepon: {kontak[nama][0]}")
        print(f"Email: {kontak[nama][1]}\n")

def cari():
    print(">>> Cari Kontak <<<")
    nama = input("Masukkan Nama Kontak: ").lower()
    if nama in kontak:
        print("--- Kontak Ditemukan ---")
        print(f"Nama: {nama}")
        print(f"Nomor Telepon: {kontak[nama][0]}")
        print(f"Alamat Email: {kontak[nama][1]}")
    else:
        print("Kontak Tidak Ditemukan.\n")

def update():
    print(">>> Update Email Kontak <<<")
    nama = input("Masukkan nama kontak: ").lower()
    if nama in kontak:
        while True:
            email_baru = input("Masukkan email baru: ").lower()
            if "@" in email_baru:
                break
            else:
              print("Email tidak valid. Silakan coba lagi.")
        kontak[nama][1] = email_baru
        print("Email berhasil diperbarui!\n")
    else:
        print("Kontak tidak ditemukan.\n")

def delete():
    nama = input("Masukkan nama kontak: ").lower()
    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus!\n")
    else:
        print("Kontak tidak ditemukan.\n")

while True:
    print("\n--- PROGRAM KONTAK ---")
    print("1. Tambah Kontak")
    print("2. Lihat Semua Kontak")
    print("3. Cari Kontak")
    print("4. Perbarui Email Kontak")
    print("5. Hapus Kontak") 
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")
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
        print("Keluar dari program. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
