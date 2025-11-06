def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    
    if jabatan.lower() == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan.lower() == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0  

    
    gaji_bersih = gaji_pokok - pajak + tunjangan

    
    print("\n===== RINCIAN GAJI KARYAWAN =====")
    print(f"Nama Karyawan   : {nama}")
    print(f"Jabatan         : {jabatan}")
    print(f"Gaji Pokok      : Rp{gaji_pokok:,.2f}")
    print(f"Pajak (5%)      : Rp{pajak:,.2f}")
    print(f"Tunjangan       : Rp{tunjangan:,.2f}")
    print(f"Gaji Bersih     : Rp{gaji_bersih:,.2f}")
    print("=================================")



nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (Manager/Staff): ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

hitung_gaji(nama, jabatan, gaji_pokok)
