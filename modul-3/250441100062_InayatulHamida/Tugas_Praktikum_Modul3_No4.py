while True:
    nama_pembeli = input("Masukkan nama pembeli: ")
    jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
    nama_barang = input("masukkan nama barang yang dibeli: ")

    total = 0
    daftar_barang = " "

    for i in range(jumlah_barang):
        nama_barang = input(f"nama barang ke {i+1}: ")
        harga = int(input(f"Masukkan harga {nama_barang}: "))
        total += harga 
        daftar_barang += f"{nama_barang} - Rp{harga}"
    
    print(nama_barang, end="")
    print("total harga: Rp", total)
    print("terima kasih telah berbelanja di IndoMie")

    lanjut = input("Apakah lanjut ke pembeli berikutnya? (y/n):")
    if lanjut.lower() != 'y':
        break
