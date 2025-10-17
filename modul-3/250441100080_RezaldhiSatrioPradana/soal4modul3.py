while True:
    nama_pembeli = input("Masukkan nama pembeli: ")

    total_harga = 0
    
    daftar_item = [] 

    print("          Warung IndoMei Struk            ")
    print(f"Nama Pembeli: {nama_pembeli}")
    
    
    while True:
        nama_barang = input("Masukkan nama barang (Ketik 'Selesai' untuk mengakhiri): ")
        
        if nama_barang.lower() == 'selesai':
            break

        
        while True:
            harga_input = input(f"Masukkan harga untuk {nama_barang}: Rp ")

            if harga_input == "":
                print("Input tidak valid! Harga tidak boleh kosong.")
                continue

            semua_angka = True
            
            
            for karakter in harga_input:
                if not karakter.isdigit(): 
                    semua_angka = False
                    break 
            
            if semua_angka:
                harga_barang = int(harga_input)
                
                
                if harga_barang < 0:
                    print(" Harga tidak boleh negatif (minus). Mohon masukkan harga yang benar.")
                    continue  
                if harga_barang == 0:
                    break 
                    
                total_harga += harga_barang
                daftar_item.append((nama_barang, harga_barang)) 
                break 
            else:
                print("Input tidak valid! Harga harus berupa angka.")

        
        if harga_input == "0" or harga_barang == 0:
            break
            
        
    if daftar_item:
        print("\n" + "="*40)
        
        print(f"{'Barang':<25}{'Harga (Rp)':>15}")
        print("-" * 40)
        
        for item, harga in daftar_item:
            print(f"{item:<25}Rp{harga:>13,}")
            
        
        print(f"{'TOTAL':<25}Rp{total_harga:>13,}") 
        print("   Terima kasih telah berbelanja di IndoMei   ")
    else:
        print("\nTidak ada barang dibeli. Struk dibatalkan.")

    
    pembeli_baru = input("Apakah ada pembeli berikutnya? (ya/tidak): ").lower()
    if pembeli_baru != "ya":
        print("\nCetak struk selesai. Program dihentikan.")
        break