def hitung_gaji(nama, jabatan, gaji_pokok):
    if jabatan == "manager":
        tunjangan = gaji_pokok * 0.10
    elif jabatan == "staff":
        tunjangan = gaji_pokok * 0.05
    else:
        tunjangan = 0

    gaji_kotor = gaji_pokok + tunjangan
    pajak = 0.05 * gaji_kotor
    gaji_bersih = gaji_kotor - pajak

    print("=== Rincian Gaji Karyawan ===")
    print("Nama Karyawan :", nama)
    print("Jabatan       :", jabatan)
    print("Gaji Pokok    : Rp", gaji_pokok)
    print("Tunjangan     : Rp", tunjangan)
    print("Gaji Kotor    : Rp", gaji_kotor)
    print("Pajak (5%)    : Rp", pajak)
    print("=" * 50)
    print("Gaji Bersih   : Rp", gaji_bersih)

nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (manager/staff): ")
gaji_pokok = int(input("Masukkan gaji pokok: "))

hitung_gaji(nama, jabatan, gaji_pokok)