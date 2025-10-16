ulang = "ya"

while ulang == "ya":
    nama = input("Masukan nama pembeli : ")
    total = 0 
    daftar = ""

    while True:
        barang = input("Masukan nama barang : ") #ketik '1' untuk mengakhiri
        if barang == "1":
            break
        while True:
            harga = float(input(f"Masukan harga {barang} : "))
            if harga <= 0 :
                print("Masukan angka yang benar")
                continue
            else :
                break
        jumlah = int(input(f"Masukan jumlah {barang} : "))
        subtotal = harga * jumlah
        total += subtotal
        daftar += f"{barang} (x{jumlah}) - Rp {subtotal:.2f}\n"

    print("\n============== Struk Belanja ==============")
    print(f"Nama Pembeli: {nama}")
    print(daftar)
    print(f"Total Belanja: Rp {total:.2f}") 
    print("Terimakasih telah berbelanja di indomei!\n")
    print("="*44)
    
    bayar = float(input("Masukan jumlah uang yang dibayar : "))
    if bayar >= total:
        kembalian = bayar - total
        print(f"Kembalian: Rp {kembalian:.2f}")
    else:
        print("Uang yang dibayar tidak cukup.") 
    print("="*44)

    ulang = input("Apakah Anda ingin mengulang? (ya/tidak) : ").lower()