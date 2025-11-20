kontak = {}

while True:
    print()
    print("MENU KONTAK")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambahkan kontak baru")
    print("4. Perbarui email pada kontak")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilih = input("Plih Menu (1-6) : ") 

    if pilih == "1":
        if kontak == {}:
            print("== Tidak ada kontak yang tersedia ==")
        else:
            for name in kontak:
                data = kontak[name]
                print(f"\u2022 Kontak {name} : Telepon = {data[0]}, Email = {data[1]}.@gmail.com")
        
    elif pilih == "2":
        name = input ("Masukkan kontak yang akan dicari : ")
        if name in kontak :
            data = kontak[name]
            print(f"\u2022 Kontak {name} : Telepon = {data[0]}, Email = {data[1]}.@gmail.com")
        else:
            print("== Kontak tidak ditemukan ==")

    elif pilih == "3" :
        name = input("Masukkan nama : " )
        if name in kontak:
            print("Kontak yang anda tambahkna sudah ada")

        else:
            telepon = input("Masukkan nomor teleponya : ")

            tlep = True
            for nomor in telepon:
                if nomor <'0' or nomor > '9':
                    tlep = False
                    break
            if tlep == False:
                print("Tolong masukkan berupa angka")
            else:
                email = input ("Masukkan email : ")
                kontak[name] = [telepon,email]

                print("Kontak telah berhasil ditambahkan")

    elif pilih == "4" :
        name = input("Masukkan nama kontak yang ingin diperbarui : ")
        if name in kontak:
            while True:
                email_baru = input("Masukkan email yang baru : ")
                if email_baru == kontak[name][1]:
                    print("Tolong gunakan email yang baru jangan gunakan email yang lama.")
                else:
                    kontak[name][1] = email_baru
                    print("Email telah berhasil diperbarui")
                    break

        else:
            print("Kontak tidak di temukan")
    
    elif pilih == "5" :
        name = input ("Masukkan kontak yang ingin ada hapus : ")
        if name in kontak:
            del kontak[name]
            print("Kontak berhasil dihapus : " )
        else:
            print("Kontak tidak ditemukan" )
    
    elif pilih == "6" :
        print("=== Program telah selesai Terima kasih === ")
        break
    else:
        print("Pilihan Tidak ada")
        print("Tolong pilih Menu yang ada di atas")