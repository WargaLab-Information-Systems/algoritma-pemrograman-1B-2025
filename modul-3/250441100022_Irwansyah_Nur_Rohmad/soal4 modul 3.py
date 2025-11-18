while True:
    print("Struk Pembelian INDOMEI")
    print("="*40)

    nama_pembeli = input("Masukkan nama pembeli :")
    print(f"Nama Pembeli : {nama_pembeli}")
    print("-"*40)
    total = 0
    while True :
        nama_barang = input("Masukkan nama barang yang dibeli :")
        if nama_barang == "SELESAI":
            break
        harga = int(input(f"Harga {nama_barang} : Rp"))
        if harga == 0:
            print("Harga tidak boleh Rp 0")
            break
        jumlah = int(input(f"Jumlah {nama_barang} : "))
        total_seluruhnya = harga * jumlah
        total = total + total_seluruhnya

        print(f"{nama_barang} Rp {harga} x {jumlah} = Rp {total_seluruhnya}")
        print(f"Total Harga Keseluruhan : Rp {total}")
        print("Terimakasih Telah Berbelanja di INDOMEI")
        print("="*40)

        ada_pembeli = input("Apakah ada pembeli selanjutnya ? (y/n) :")
        if ada_pembeli == "n":
            print("Okeyy Sampai Jumpa Lagi :D")
            break
        else :
            continue