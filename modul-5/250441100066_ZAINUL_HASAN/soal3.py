def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok
    if jabatan == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0

    gaji_bersih = gaji_pokok - pajak + tunjangan
    
    print("Nama       :", nama)
    print("Jabatan    :", jabatan)
    print("Gaji Pokok :", gaji_pokok)
    print("Pajak (5%) :", pajak)
    print("Tunjangan  :", tunjangan)
    print("Gaji Bersih:", gaji_bersih)

nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (Manager/Staff): ")
gaji_pokok = float(input("Masukkan gaji pokok: "))

hitung_gaji(nama, jabatan, gaji_pokok)