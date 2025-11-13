a_list = []
def cek_sama(daftar):
    total = 0
    for a in daftar:
        total += a

    if total % 2 != 0:
        return False
    
    setengah = total // 2
    jumlah = 0
    for a in daftar:
        jumlah += a
        if jumlah == setengah:
            return True
    return False

while True:
    print("\n=== program cek list ===")
    print("1.tambah angka")
    print("2.tampilkan angka")
    print("3.ubah angka")
    print("4.hapus angka")
    print("5.cek dua bagian sama")
    print("6.keluar")
    
    pilihan = input("pilih menu:")

    if pilihan  == "1":
        angka = int(input("masukkan angka:"))
        a_list.append(angka)
        print("data berhasil ditambah")

    elif pilihan == "2":
        print("daftar angka:", a_list)

    elif pilihan == "3":
        idx = int(input("masukkan indeks yang ingin diubah:"))
        if 0 <= idx < len(a_list):
            baru = int(input("masukkan nilai baru:"))
            a_list[idx] = baru
            print("data berhasil diubah")
        else:
            print("indeks tidak valid")

    elif pilihan == "4":
        idx = int(input("masukkan indeks yang ingin dihapus:"))
        if 0 <= idx < len(a_list):
            del a_list[idx]
            print("data berhasil dihapus")
        else:
            print("indeks tidak valid")

    elif pilihan == "5":
        if len(a_list) == 0:
            print("Daftar masih kosong, tambahin datanya dulu!")
        else:
            hasil = cek_sama(a_list)
            total = 0
            for a in a_list:
                total += a
            if total % 2 == 0:
                setengah = total // 2
                jumlah = 0
                for i in range(len(a_list)):
                    jumlah += a_list[i]
                    if jumlah == setengah:
                        kiri = a_list[:i+1]
                        kanan = a_list[i+1:]
                        print(kiri, kanan)
                        break

            print("hasil:", hasil)

    elif pilihan == "6":
        print("program selesai")
        break

    else:
        print("pilihan tidak valid")
