contacts = {} 
 
while True:
    print("\n=== MENU ===")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak")
    print("4. Perbarui email")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1": 
        kosong = True
        for nama in contacts:   
            kosong = False
            break

        if kosong:
            print("Belum ada kontak.")
        else:
            print("\n=== Daftar Kontak ===")
            for nama in contacts:           
                nomor = contacts[nama][0]   
                email = contacts[nama][1]
                print(f"Nama: {nama} | Nomor: {nomor} | Email: {email}")   
                

    
    elif pilihan == "2": 
        nama_cari = input("Masukkan nama kontak: ")

        if nama_cari in contacts:   
            print("\nKontak ditemukan!")
            print("Nama :", nama_cari)
            print("Nomor:", contacts[nama_cari][0])
            print("Email:", contacts[nama_cari][1])
        else:
            print("Kontak tidak ditemukan.")

    
    elif pilihan == "3": 
        nama = input("Masukkan nama: ")
        while True:
            nomor = input("Masukkan nomor: ")
            valid = True
            for angka in nomor:              
                if angka not in "0123456789":
                    valid = False
                    break

            if valid:
                nomor = int(nomor)
                break
            print("Tidak valid! Nomor harus angka.")

        email = input("Masukkan email: ")
        if "@gmail.com" not in email:
            email += "@gmail.com"

        contacts[nama] = [nomor, email]   
        print("Kontak berhasil ditambahkan!")

    
    elif pilihan == "4":
        if not contacts:
            print("Belum ada kontak.")
        else:
            print("\n=== Daftar Kontak ===")
            for nama in contacts:           
                nomor = contacts[nama][0]   
                email = contacts[nama][1]
                print(f"Nama: {nama} | Nomor: {nomor} | Email: {email}")   

            nama_up = input("\nMasukkan nama kontak: ")

        if nama_up in contacts:

            email_baru = input("Masukkan email baru: ")
            if "@gmail.com" not in email_baru:
                email_baru += "@gmail.com"

            contacts[nama_up][1] = email_baru   
            print("Email berhasil diperbarui!")
        else:
            print("Kontak tidak ditemukan.")

    
    elif pilihan == "5":
        nama_hapus = input("Masukkan nama kontak: ")

        if nama_hapus in contacts:
            del contacts[nama_hapus]   
            print("Kontak berhasil dihapus.")
        else:
            print("Kontak tidak ditemukan.")

   
    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")
