data = []
id_auto = 1

while True:
    print("1. Tambah Kunjungan")
    print("2. Tampilkan Kunjungan")
    print("3. Hapus Kunjungan")
    print("4. Keluar")
    print()
    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama pengunjung: ")
        santri = input("Nama santri: ")
        daerah = input("Daerah (Sumatra/Kalimantan/Jawa/Papua): ")
        data.append([id_auto, nama, santri, daerah])
        print("Data ditambahkan ID : ", (id_auto))
        id_auto += 1

    elif pilih == "2":
        if not data:
            print("Belum ada data.")
        else:
            for e in ["Sumatra", "Kalimantan", "Jawa", "Papua"]:
                print(f"\n--- {e} ---")
                ada = False
                for i in data:
                    if i[3].lower() == e.lower(): 
                        print(f"ID:{i[0]} | Pengunjung:{i[1]} | Santri:{i[2]}")
                        ada = True
                if not ada:
                    print("Tidak ada pengunjung dari daerah ini.")

    elif pilih == "3":
        id_hapus = input("Masukkan ID yang ingin dihapus: ")
        if id_hapus.isdigit():
            id_hapus = int(id_hapus)
            ditemukan = False
            for i in data:
                if i[0] == id_hapus:
                    data.remove(i)
                    print("Data berhasil dihapus.")
                    ditemukan = True
                    break
            if not ditemukan:
                print("ID tidak ditemukan.")
        else:
            print("ID harus berupa angka!")

    elif pilih == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")