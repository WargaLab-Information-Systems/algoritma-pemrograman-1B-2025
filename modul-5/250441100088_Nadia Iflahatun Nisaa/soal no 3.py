def hitung_gaji(nama, jabatan, gaji_pokok):
    pj = gaji_pokok * 0.05

    if jabatan == "manager":
        tunjangan = gaji_pokok * 0.10
    elif jabatan == "staff":
        tunjangan = gaji_pokok * 0.05
    else:
        tunjangan = 0

    gaji_bersih = gaji_pokok - pj + tunjangan

    print("nama karyawan:", nama)
    print("jabatan:", jabatan)
    print("gaji pokok:", gaji_pokok)
    print("pajak 5%:", pj)
    print("tunjangan:", tunjangan)
    print("gaji bersih:", gaji_bersih)

nama = input("masukkan nama karyawan:")
jabatan = input("jabatan(manager or staff?):")
gaji_pokok = float(input("masukkan gaji pokok:"))

hitung_gaji(nama, jabatan, gaji_pokok)