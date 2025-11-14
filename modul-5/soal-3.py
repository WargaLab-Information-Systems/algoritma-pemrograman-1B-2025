def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok

    if jabatan == "manager":
        tunjangan = gaji_pokok * 0.10
    elif jabatan == "staff":
        tunjangan = gaji_pokok * 0.05
    else:
        tunjangan = 0

    gaji_bersih = gaji_pokok + tunjangan - pajak

    print("=== Rincian Gaji Karyawan ===")
    print("Nama Karyawan :", nama)
    print("Jabatan       :", jabatan)
    print("Gaji Pokok    : Rp", gaji_pokok)
    print("Tunjangan     : Rp", tunjangan)
    print("Pajak (5%)    : Rp", pajak)
    print("=" * 50)
    print("Gaji Bersih   : Rp", gaji_bersih)

nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (manager/staff): ")
gaji_pokok = int(input("Masukkan gaji pokok: "))

hitung_gaji(nama, jabatan, gaji_pokok)
