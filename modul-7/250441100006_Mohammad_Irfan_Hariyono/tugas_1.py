def menu():
    print("\n Menu Kontak ")
    print("1. Tambah kontak baru ")
    print("2. Tampilkan semua kontak")
    print("3. Perbarui email kontak ")
    print("4. Hapus kontak ")
    print("5. Cari kontak ")
    print("6. Keluar ")

def tambah_kontak(buku_kontak):
    print("\n Tambah kontak baru ")
    while True:
        nama = input("Masukkan nama : ")
        if len(nama) == 0:
            print("Nama ini tidak boleh kosong")
            continue

        ada_angka = False
        for angka in nama:
            if angka.isdigit():
                ada_angka = True
                break

        if ada_angka:
            print("Nama harus berupa huruf saja! (Tidak boleh ada angka)")
            continue
        if nama in buku_kontak:
            print(f"Kontak dengan nama '{nama}' sudah ada. Gunakan menu update jika ingin merubah yaa >_<")
        else:
            break
    while True:
        telepon = input("Masukkan nomor telepon harus 12 digit yaa : ")

        if not telepon.isdigit():
            print("Error : Input harus berupa angka saja")
        elif len(telepon) != 12:
            print(f"Error : Nomor harus pas 12 digit (kamu malah masukin {len(telepon)})")
        else:
            break
    while True:
        email = input(f"Masukkan email : ")

        harus = "@gmail.com"
        if harus not in email :
            print(f"ini bukan email (harus pakai  {harus}) dibelakangnya")
            continue
        email_ada = False
        for info in buku_kontak.values():
            if email == info[1]:
                email_ada = True
                break
        if email_ada :
            print("Error : Email ini sudah terdaftar di kontak lain. Masukkan email baru")
        else:
            break

    buku_kontak[nama] = [telepon, email]
    print(f"Yeayyy kontak '{nama}' berhasil ditambahkan.")

def tampilkan(buku_kontak):
    print("\n Daftar semua kontak ")
    if not buku_kontak :
        print("Buku kontak masih kosong.")
        return
    
    for nama, info in buku_kontak.items():
        telepon = info [0] 
        email = info [1]
        
        print(f"Nama    : {nama}")
        print(f"Telepon : {telepon}")
        print(f"Email   : {email}")
        print("\n")

def update_email(buku_kontak):
    nama =input(f"Masukkan nama kontak yang email nya ingin di rubah ")
    
    if nama in buku_kontak:
        email_lama = buku_kontak[nama][1]

        while True:
            email_baru = input(f"Masukkan email baru untuk {nama} : ")
            if email_baru == email_lama:
                print(f"Email '{email_baru}' sudah dipakai, Masukkan email yang berbeda")
                continue

            email_sudah_ada = False
            for pemilik, info in buku_kontak.items():
                if info[1] == email_baru and pemilik != nama:
                    email_sudah_ada = True
                    break
            if email_sudah_ada:
                print(f"Gagal! Email '{email_baru}' sudah dipakai orang lain. Coba email lain.")
            else:
                buku_kontak[nama][1] = email_baru
                print(f"Email untuk '{nama}' berhasil diperbarui menjadi {email_baru}")
                break
    else:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan ")

def hapus_kontak(buku_kontak):
    nama = input("Masukkan nama kontak yang ingin dihapus : ")
    if buku_kontak.pop(nama, None) is not None:
        print(f"Kontak '{nama}' berhasil dihapus ")
    else:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan ")

def cari_kontaks(buku_kontak):
    nama_dicari = input("Masukkan kata kunci yang ingin dicari : (bisa nama, nomer telepon, email) ").lower()
    bendera = False

    for nama, info in buku_kontak.items():
        telepon_x = info[0]
        email_x = info[1].lower()
        nama_x = nama.lower()

        if nama_dicari in nama_x or nama_dicari == telepon_x or nama_dicari in email_x:

            print(f"\n Detail kontak : {nama_dicari} ")
            print(f"Nama    : {nama}")
            print(f"Telepon : {telepon_x}")
            print(f"Email   : {info[1]}")

            bendera = True
    if not bendera:
        print(f"Kontak dengan nama '{nama_dicari}' tidak ditemukan. ")

def inti():
    buku_kontak = {}
    
    while True:
        menu()
        milih_mana = input("Silakan pilih menu (1-6) : ")
        
        if milih_mana == "1":
            tambah_kontak(buku_kontak)
        elif milih_mana == "2":
            tampilkan(buku_kontak)
        elif milih_mana == "3":
            update_email(buku_kontak)
        elif milih_mana == "4":
            hapus_kontak(buku_kontak)
        elif milih_mana == "5":
            cari_kontaks(buku_kontak)
        elif milih_mana == "6":
            print("Kamu keluar program ")
            break
        else:
            print("Pilihan mu tidak ada di menu. Silakan pilih lagi (1-6)")

inti()