data_angka = []

def tambah_angka():
  while True:
    angka = input("Masukkan angka: ")
    try:
        angka = int(angka)
        data_angka.append(angka)
        print("Data ditambahkan")
        break
    except ValueError:
        print("Input tidak valid! Harus berupa angka, coba lagi.")
    
def tampilkan_data():
    print("data saat ini: ", data_angka)

def ubah_data():
    if len(data_angka) == 0:
        print("Belum ada data yang bisa diubah.")
        return
    while True:
        indeks = input("Masukkan indeks data yang ingin diubah: ")
        try:
            indeks = int(indeks)
            if 0 <= indeks < len(data_angka):
                while True:
                    baru = input("Masukkan nilai baru: ")
                    try:
                        baru = int(baru)
                        data_angka[indeks] = baru
                        print("Data berhasil diubah")
                        return
                    except ValueError:
                        print("Input tidak valid! Nilai baru harus berupa angka.")
            else:
                print("Indeks tidak ditemukan")
                return
        except ValueError:
            print("Input indeks harus berupa angka! Coba lagi.")
    
def hapus_data():
    if len(data_angka) == 0:
        print("Belum ada data yang bisa dihapus")
        return
    
    while True:
        indeks = input("Masukkan indeks data yang ingin dihapus: ")
        try:
          indeks = int(indeks)
          if 0 <= indeks < len(data_angka):
            del data_angka[indeks]
            print("Data berhasil dihapus")
            break
          else:
            print("Indeks tidak ditemukan")
            break
        except ValueError:
            print("Input harus berupa angka! Coba lagi.")

def cek_pembagian():
    if len(data_angka) == 0:
        print("Belum ada data untuk diperiksa.")
        return

    total = sum(data_angka)
    if total % 2 != 0:
        print("False (total tidak bisa dibagi dua sama besar)")
        return

    setengah_total = total // 2
    hasil_kelompok_angka = []

    # untuk mencari kombinasi yang bisa menghasilkan setengah total
    def cek_bagi_dua(i, jumlah, kelompok_angka):
        if jumlah == setengah_total:
           for angka in kelompok_angka:
               hasil_kelompok_angka.append(angka)
           return True
        if i >= len(data_angka) or jumlah > setengah_total:
            return False
        
        # coba ambil angka ke-i
        if cek_bagi_dua(i + 1, jumlah + data_angka[i], kelompok_angka + [data_angka[i]]):
            return True
        # atau lewati angka ke-i
        return cek_bagi_dua(i + 1, jumlah, kelompok_angka)

    hasil = cek_bagi_dua(0, 0, [])
    print("Dapat dibagi menjadi dua bagian dengan jumlah sama:", hasil)
    if hasil:
        print("Salah satu kelompok angka:", hasil_kelompok_angka)

while True:
    print("=====PROGRAM PEMBAGIAN DERET ANGKA =====")
    print("1. tambah angka") # create
    print("2. tampilkan data") # read
    print("3. ubah data") # update
    print("4. hapus data") # delate
    print("5. cek pembagian")
    print("6. keluar")
    pilihan = input("pilihan menu: ")
    if pilihan not in ["1", "2", "3", "4", "5", "6"]:
        print("Pilihan tidak valid! Masukkan angka 1 sampai 6")
        continue

    if pilihan == "1":
        tambah_angka()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        cek_pembagian()
    elif pilihan == "6":
        break


