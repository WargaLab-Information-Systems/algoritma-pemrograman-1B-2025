while True:
    nama = input("Masukkan Nama Pembeli: ")
    jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
    
    total_harga = 0
    daftar_barang = "" 
    
    for i in range(jumlah_barang):
        nama_barang = input(f"Nama barang ke {i+1}: ")
        harga = int(input(f"Harga {nama_barang}: "))
        total_harga += harga
        daftar_barang += f"{nama_barang} : Rp {harga}\n" 

    next=("Apakah anda pembeli selanjutnya (ya/tidak) :") 
    if next == "tidak":
        break
    
    print("="*100)
    print("==== STRUK PEMBELIAN INDOMEI ===")
    print("Nama pembeli :", nama)
    print("="*100)
    print("Daftar barang dan harga yang dibeli :")
    print(daftar_barang, end="") 
    print("="*100)
    print("Total harga: Rp", total_harga)
    print("Terima kasih telah berbelanja di IndoMei.")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lanjut == "n":
        print("Selesai.")
        break