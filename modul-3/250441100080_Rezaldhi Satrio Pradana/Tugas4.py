while True:
    nama_pembeli = input("Masukkan nama pembeli: ")
    total_harga = 0
    daftar_item = []
    print(" Warung IndoMei Struk ")
    print(f"Nama Pembeli: {nama_pembeli}")
    while True:
        nama_barang = input("Masukkan nama barang (Ketik 'Selesai' untuk mengakhiri): ")
        if nama_barang.lower() == 'selesai':
            break
        while True:
            harga_input = input(f"Masukkan harga untuk{nama_barang}: Rp ")
            if harga_input == "":
                print("Input tidak valid! Harga tidak bolehkosong.")
                continue
            semua_angka = True
            for karakter in harga_input:
                if not karakter.isdigit():
                    semua_angka = False
                    break
            if semua_angka:
                harga_barang = int(harga_input)
            if harga_barang < 0:
                print(" Harga tidak boleh negatif (minus).Mohon masukkan harga yang benar.")