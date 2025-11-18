# Program menghitung gaji bersih karyawan

def hitung_gaji():
    nama = input("Masukkan nama karyawan: ")
    jabatan = input("Masukkan jabatan (manager/staff): ")
    gaji = float(input("Masukkan gaji pokok: "))

    pajak = 0.05 * gaji

    if jabatan.lower() == "manager":
        tunjangan = 0.10 * gaji
    elif jabatan.lower() == "staff":
        tunjangan = 0.05 * gaji
    else:
        tunjangan = 0

    gaji_bersih = gaji - pajak + tunjangan

    print("\n=== Hasil Perhitungan ===")
    print("Nama Karyawan :", nama)
    print("Jabatan       :", jabatan)
    print("Gaji Pokok    : Rp", gaji)
    print("Pajak (5%)    : Rp", pajak)
    print("Tunjangan     : Rp", tunjangan)
    print("Gaji Bersih   : Rp", gaji_bersih)

hitung_gaji()
