ulang = "y"  # agar program bisa diulang

while ulang == "y":
    print("=== STRUK PEMBELIAN INDOMEI ===")

    nama = input("Masukkan nama pembeli: ")

    total_harga = 0  
    daftar_barang = ""  

    # input data barang
    while True:
        barang = input("Masukkan nama barang (ketik 'selesai' untuk berhenti): ")

        if barang.lower() == "selesai":
            break

        harga = int(input("Masukkan harga barang: "))

        daftar_barang += f"- {barang} : Rp{harga}\n"  
        total_harga += harga  

    # tampilkan struk
    print("\n----- STRUK PEMBELIAN -----")
    print("Nama Pembeli:", nama)
    print("---------------------------")
    print("Daftar Barang:")
    print(daftar_barang, end="")  
    print("---------------------------")
    print("Total Harga : Rp", total_harga)
    print("Terima kasih telah berbelanja di IndoMei!")
    print("---------------------------\n")

    ulang = input("Apakah ada pembeli berikutnya? (y/n): ").lower()

print("Program selesai. Sampai jumpa!")
