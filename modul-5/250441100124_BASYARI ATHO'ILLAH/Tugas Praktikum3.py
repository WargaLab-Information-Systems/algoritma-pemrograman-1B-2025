# ppph -> 0.05
# inputannya -> nama, jabatan, gaji pokok
# tunjangan jabatan -> 10% jika manajer, 5% jika staf

def identitas(nama, jabatan, gaji):
    print("\n=== Rincian Gaji Karyawan ====")
    print("Nama Karyawan:", nama)
    print("Jabatan:", jabatan)
    print("Gaji Pokok: Rp:", gaji)
    print("Pajak PPh (5%): Rp:", pph(gaji))
    print("Tunjangan Jabatan: Rp:", tunjangan(jabatan))
    total_gaji = gaji - pph(gaji) + tunjangan(jabatan)
    print("Total Gaji Bersih: Rp:", total_gaji)
    
def pph(gaji):
    pph = 0.05
    pajak = gaji * pph
    return pajak

def tunjangan(jabatan):
    if jabatan == "manager":
        return gaji * 0.10
    elif jabatan == "staff":
        return gaji * 0.05
    else:
        return 0
    
nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (manager/staff): ").lower()
gaji = int(input("Masukkan gaji pokok: "))
kumpulan = identitas(nama, jabatan, gaji)
