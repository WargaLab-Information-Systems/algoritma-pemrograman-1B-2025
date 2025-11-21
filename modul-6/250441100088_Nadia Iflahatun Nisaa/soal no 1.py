d_kunjungan = []
id_atrian = 1

while True:
    print("=== sistem kunjungan santri ===")
    print("1.tambah data pengunjung")
    print("2.tampilkan semua data pengunjung")
    print("3.hapus data pengunjung")
    print("4.keluar")

    pilihan = input("pilih menu:")

    if pilihan == "1":
        nm_pengunjung = input("nama pengunjung:")
        nm_santri = input("nama santri yang dikunjungi:")
        daerah = input("daerah asal(sumatra/kalimantan/jawa):")

        d_kunjungan.append([id_atrian, nm_pengunjung, nm_santri, daerah])
        print("data berhasil ditambahkan dengan id antrian:", id_atrian)
        id_atrian += 1

    elif pilihan == "2":
        print("daftar kunjungan santri")
        urut_daerah = ["sumatra", "kalimantan", "jawa"]
        for daerah in urut_daerah:
            print(f"daerah: {daerah}")
            for data in d_kunjungan:
                if data[3] == daerah:
                    print(f"id:{data[0]} | pengunjung: {data[1]} | santri: {data[2]}")
    elif pilihan == "3":
        hapus = int(input("masukkan id santri yang ingin dihapus:"))
        ditemukan = False
        for data in d_kunjungan:
            if data[0] == hapus:
                d_kunjungan.remove(data)
                ditemukan = True
                print("data berhasil dihapus")
                break
        if not ditemukan:
            print("id tidak ditemukan")
    elif pilihan == "4":
        print("program selesai")
        print(d_kunjungan)
        break
    else:
        print("pilihan tidak valid")

    