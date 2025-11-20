kontak = {}

def tampilkan_kontak():
    if not kontak:
        print("Tidak ada kontak.")
    else:
        for nama, info in kontak.items():
            print(f"Nama: {nama}, Nomor Telepon: {info[0]}, Email: {info[1]}@gmail.com")

def cari():
    nama = input("Masukkan nama/no/email yang ingin dicari: ")
    for Nama, info in kontak.items():
        if info[0] == nama or info[1] == nama or Nama == nama:
            print(f"Nama: {Nama}, Nomor Telepon: {info[0]}, Email: {info[1]}@gmail.com")
            ditemukan = True
            break
    if not ditemukan:
            print(f"{nama} tidak valid.")
    
def tambah_kontak():
    while True:
        nama = input("Masukkan nama kontak: ")
        break
    while True:
        nomor_telepon = input("Masukkan nomor telepon: ")
        if not nomor_telepon.isdigit():
            print("Nomor telepon harus berupa angka.")
        elif len(nomor_telepon) == 12:
            print("nomor telepon berhasil ditambahkan.")
            break
        else:
            print("nomor salah, coba lagi")  
    while True:
        email = input("Masukkan email: ")
        email_sudah_ada = False
        for kontak_lain in kontak:
            if kontak_lain != email and kontak[kontak_lain][1] == email:
                email_sudah_ada = True
                break
        if email_sudah_ada:
            print("Email sudah digunakan oleh kontak lain. Silakan masukkan email yang berbeda.")
        elif email.endswith("@gmail.com"):
            kontak[nama] = [nomor_telepon, email]
            print("email berhasil ditambahkan")
            print("kontak berhasil di tambahkan")
            break 
        else:
            print("email harus berakhiran @gmail.com")
    
def perbarui_email():
    nama = input("Masukkan nama kontak yang ingin diperbarui emailnya: ")
    if nama in kontak:
        while True: 
            email_baru = input("Masukkan email baru: ")
            email_sudah_ada = False
            for kontak_lain in kontak:
                if kontak_lain != nama and kontak[kontak_lain][1] == email_baru:
                    email_sudah_ada = True
                    break
            if email_sudah_ada:
                print("Email sudah digunakan oleh kontak lain. Silakan masukkan email yang berbeda.")
            else:
                kontak[nama][1] = email_baru
                print("Email berhasil diperbarui.")
                break  
    else:
        print("Kontak tidak ditemukan.")
        
def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")
        
def menu():
    while True:
        print("\nMenu Contact Book:")
        print("1. Tambah kontak baru")
        print("2. Tampilkan semua kontak")
        print("3. Cari kontak")
        print("4. Perbarui email kontak")
        print("5. Hapus kontak")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            tambah_kontak()
        elif pilihan == '2':
            tampilkan_kontak()
        elif pilihan == '3':
            cari()
        elif pilihan == '4':
            perbarui_email()
        elif pilihan == '5':
            hapus_kontak()
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()