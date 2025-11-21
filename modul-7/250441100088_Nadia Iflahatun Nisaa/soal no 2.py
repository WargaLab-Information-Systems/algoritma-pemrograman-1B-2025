inventaris = {}  

while True:
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang")
    print("3. Tambah barang")
    print("4. Update stok")
    print("5. Hapus barang")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    
    if pilihan == "1":
        kosong = True
        for id_b in inventaris:
            kosong = False
            break

        if kosong:
            print("Belum ada barang.")
        else:
            print("\n=== DAFTAR BARANG ===")
            for id_b in inventaris:
                nama = inventaris[id_b][0]
                harga = inventaris[id_b][1]
                stok = inventaris[id_b][2]
                print(f"ID: {id_b} | Nama: {nama} | Harga: {harga} | Stok: {stok}")

                
    
    elif pilihan == "2":
        id_cari = input("Masukkan ID barang: ")

        if id_cari in inventaris:
            print("\nBarang ditemukan!")
            print("ID   :", id_cari)
            print("Nama :", inventaris[id_cari][0])
            print("Harga:", inventaris[id_cari][1])
            print("Stok :", inventaris[id_cari][2])
        else:
            print("Barang tidak ditemukan.")

    
    elif pilihan == "3":
        id_baru = input("Masukkan ID barang: ")
        nama = input("Masukkan nama barang: ")
        while True:
            harga = input("Masukkan harga barang: ")
            valid = True
            for angka in harga:
                if angka not in "0123456789":
                    valid = False
                    break
                
            if valid:
                harga = int(harga)
                break
            print("Harga tidak valid! Harus angka.")

        while True:
            stok = input("Masukkan stok barang: ")
            valid = True
            for angka in stok:
                if angka not in "0123456789":
                    valid = False
                    break

            if valid:
                stok = int(stok)
                break
            print("Stok tidak valid! Harus angka.")

        inventaris[id_baru] = [nama, harga, stok]
        print("Barang berhasil ditambahkan.")

    
    elif pilihan == "4":
        if kosong:
            print("Tidak ada item yang terdaftar.")
        else:
            print("\n================ DAFTAR BARANG ================")
            for id_b in inventaris:
                nama = inventaris[id_b][0]
                harga = inventaris[id_b][1]
                stok = inventaris[id_b][2]
                print(f"ID: {id_b} | Nama: {nama} | Harga: {harga} | Stok: {stok}")

            id_up = input("\nMasukkan ID barang: ")

        if id_up in inventaris:
            while True:
                stok_baru = input("Masukkan stok baru: ")
                valid = True
                for angka in stok_baru:
                    if angka not in "0123456789":
                        valid = False
                        break

                if valid:
                    stok_baru = int(stok_baru)
                    break

                print("Stok tidak valid! Harus angka.")

            if stok_baru < 0:
                print("Stok tidak boleh negatif!")
            else:
                inventaris[id_up][2] = stok_baru
                print("Stok berhasil diperbarui.")
        else:
            print("Barang tidak ditemukan.")

    
    elif pilihan == "5":
        id_del = input("Masukkan ID barang: ")

        if id_del in inventaris:
            del inventaris[id_del]
            print("Barang berhasil dihapus.")
        else:
            print("Barang tidak ditemukan.")

    
    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")