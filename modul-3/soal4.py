lagi = "y"
while lagi:
    print(" SELAMAT BER BELANJA ")
    nama = input("masukkan nama anda ")
    banyak_barang = int(input("masukkan banyak barang "))
    total = 0
    daftar = " "
    for i in range(1,banyak_barang + 1):
        nama_barang = input(f"masukkan nama barang ke - {i}" )
        harga = int(input(f"masukkan harga barang ke - {i} "))
        total += harga
        daftar += f" nama barang {nama_barang} Rp : {harga}"
    print("="*5," STRUK ", "="*5)
    print("Nama Pembeli :", nama)
    print("Daftar barang :")
    print(daftar)
    print("Total harga ",total)
    print("="*5, "TERIMA KASIH", "="*5)

    lagi = input("Apakah ada pelanggan selanjutnya ? (y/n)")
    if lagi == "n":
        break  