inventaris = {}
while True:
    print()
    print("=== Menu Inventaris Barang ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang (Gunakan ID barang)")
    print("3. Tambahkan barang baru")
    print("4. Perbarui stok barang")
    print("5. Hapus barang")
    print("6. Keluar")

    pilih = input("Pilih Menu (1-6) : ")

    if pilih == "1" :
        if inventaris == {}:
            print("== Tidak ada barang didalam inventaris ==")
        else:
            for id in inventaris :
                data = inventaris [id]
                print(f"\u2022 ID: {id} : Nama Barang {data[0]}, Harga = Rp{data[1]}, Stok = {data[2]}")

    elif pilih == "2" :
        id = input("masukkan id barang yang dicari: ")
        if  id in inventaris:
            data = inventaris[id]

            print(f"\u2022 ID: {id}, Nama Barang: {data[0]}, Harga: Rp{data[1]}, Stok: {data[2]}")
        else:
            print("id barang tidak ditemukan")

    elif pilih == "3" :
        nama = input("masukkan nama barang: ")
        id = input("masukkan id barang: ")
        if id in inventaris:
            print("id barang sudah ada")
        
        else:
            harga =input("Masukkan harga barang :  ")

            harganya = True
            for angka in harga:
                if angka < '0' or angka > '9':
                    harganya = False
                    break

            if harganya == False:
                print("tolong masukkan berupa angka dan jangan masukan angka negatif ataupun simbol")

            else:
                stok = input("masukkan stok barang: ")
                inventaris[id] = [nama, harga, stok]
                
                print("barang berhasil ditambahkan")

    elif pilih == "4" :
        id = input("masukkan id yang mau diperbarui: ")
        if id in inventaris:
            baru = input("masukkan stok baru:")
            stoknya = True
            for nomor in baru:
                if nomor < '0' or nomor > '9':
                    stoknya = False
                    break

            if stoknya == False:
                print("Tolong masukkan berupa angka dan jangan masukan angka negatif ataupun simbol")
            else:
                inventaris[id][2] = baru
                print("stok berhasil diperbarui")
        else:
            print("id barang tidak ditemukan")

    elif pilih == "5" :
        id = input("masukkan id yang mau dihapus: ")
        if id in inventaris:
            del inventaris[id]
            print("barang berhasil dihapus")
        else:
            print("id barang tidak ditemukan")

    elif pilih == "6" :
        print("program selesai, Terimakasih")
        break
    else:
        print("Tolong pilih menu yang tersedia.")