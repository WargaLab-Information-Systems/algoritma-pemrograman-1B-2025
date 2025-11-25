Contacts = {}

def tampilkan_kontak():
    if not Contacts:
        print("Kontak kosong.")
    else:
        kontak_terurut = sorted(Contacts.items()) 
        
        print("\n=== DAFTAR KONTAK SAAT INI ===")
        nomor = 1
        for nama, info in kontak_terurut:
            print(f"{nomor}. {nama}: Telepon = {info[0]}, Email = {info[1]}") 
            nomor += 1
    print()

def cari_kontak():
    while True: 
        nama = input("Masukkan nama kontak yang ingin dicari: ")
        if not nama.strip() or not all(c.isalpha() or c.isspace() for c in nama.strip()):
            print("Input tidak valid. Nama kontak harus berupa huruf (bukan angka/simbol).")
            continue 
        break 

    if nama in Contacts:
        print(f"Kontak Ditemukan: {nama}: Telepon = {Contacts[nama][0]}, Email = {Contacts[nama][1]}")
    else:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan.")
    print()

def validasi_nama_manual(nama):
    if not nama.strip():
        return False
    
    for karakter in nama:
        if not karakter.isalpha() and not karakter.isspace():
            return False
    return True

def validasi_telepon(telepon):
    """Memastikan telepon hanya angka dan memiliki panjang 10-13 digit."""
    if not telepon.isdigit():
        print(" Input tidak valid. Nomor telepon hanya boleh mengandung angka.")
        return False
    
    panjang = len(telepon)
    if not (10 <= panjang <= 13):
        print(f" Input tidak valid. Nomor telepon harus 10 sampai 13 digit. (Panjang saat ini: {panjang})")
        return False
        
    return True

def tambah_kontak():
    while True:
        nama = input("Masukkan nama kontak baru: ")
        if validasi_nama_manual(nama):
            break
        else:
            print(" Input tidak valid. Nama kontak harus berupa huruf saja, tidak boleh ada angka atau simbol.")

    if nama in Contacts:
        print("Kontak sudah ada.")
        print()
        return 

    while True:
        telepon = input("Masukkan nomor telepon (10-13 digit): ")
        if validasi_telepon(telepon):
            break

    while True:
        email = input("Masukkan email: ")
        if "@gmail" in email and "." in email:
            break
        else:
            print("Input tidak valid. Email harus mengandung '@gmail' dan '.'.")
    
    Contacts[nama] = [telepon, email]
    print(f"Kontak '{nama}' berhasil ditambahkan.")
    print()

def perbarui_telepon():

    tampilkan_kontak() 
    
    nama = input("Masukkan nama kontak yang ingin diperbarui nomor teleponnya: ")
    if nama in Contacts:
        telepon_lama = Contacts[nama][0]
        email_info = Contacts[nama][1]
        print(f"\nKontak ditemukan: {nama} (Telepon lama: {telepon_lama}, Email: {email_info})")
        
        while True:
            telepon_baru = input("Masukkan nomor telepon baru (10-13 digit): ")
            if validasi_telepon(telepon_baru):
                break
                
        Contacts[nama][0] = telepon_baru
        print(f"Nomor telepon untuk kontak '{nama}' berhasil diperbarui dari {telepon_lama} menjadi {telepon_baru}.")
    else:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan.")
    print()

def perbarui_email():
    tampilkan_kontak()
    
    nama = input("Masukkan nama kontak yang ingin diperbarui emailnya: ")
    if nama in Contacts:
        email_lama = Contacts[nama][1]
        telepon_info = Contacts[nama][0]
        print(f"\nKontak ditemukan: {nama} (Telepon: {telepon_info}, Email lama: {email_lama})")
        
        while True:
            email_baru = input("Masukkan email baru: ")
            if "@gmail" in email_baru and "." in email_baru:
                break
            else:
                print("Input tidak valid. Email harus mengandung '@gmail' dan '.'.")
                
        Contacts[nama][1] = email_baru
        print(f" Email untuk kontak '{nama}' berhasil diperbarui dari {email_lama} menjadi {email_baru}.")
    else:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan.")
    print()

def hapus_kontak():
    tampilkan_kontak() 
    
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    if nama in Contacts:
        info = Contacts[nama]
        print("\n--- DETAIL KONTAK YANG AKAN DIHAPUS ---")
        print(f"- Nama: {nama}")
        print(f"- Telepon: {info[0]}")
        print(f"- Email: {info[1]}")
        
        konfirmasi = input("Apakah Anda yakin ingin menghapus kontak ini? (y/n): ").lower()
        
        if konfirmasi == 'y':
            del Contacts[nama]
            print(f"Kontak '{nama}' berhasil dihapus.")
        else:
            print(f"Pembatalan. Kontak '{nama}' tidak jadi dihapus.")
    else:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan.")
    print()

def menu():
    while True:
        print("=== MENU KONTAK ===")
        print("1. Tampilkan semua kontak")
        print("2. Cari kontak")
        print("3. Tambah kontak")
        print("4. Perbarui nomor telepon kontak")
        print("5. Perbarui email kontak")
        print("6. Hapus kontak")
        print("7. Keluar")
        pilihan = input("Pilih menu (1-7): ")

        if pilihan == '1':
            tampilkan_kontak()
        elif pilihan == '2':
            cari_kontak()
        elif pilihan == '3':
            tambah_kontak()
        elif pilihan == '4':
            perbarui_telepon() 
        elif pilihan == '5':
            perbarui_email()
        elif pilihan == '6':
            hapus_kontak()
        elif pilihan == '7':
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid (Hanya masukkan angka 1-7). Silakan coba lagi.\n")

menu()

