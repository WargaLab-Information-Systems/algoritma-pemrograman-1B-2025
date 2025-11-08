# Tunjangan jabatan -> 10% jika manajer, 5% jika staf

def identitas(nama, jabatan, gaji):
    print("\n===== Rincian Gaji Karyawan =====")
    print("Nama Karyawan     :", nama)
    print("Jabatan           :", jabatan)
    print("Gaji Pokok        : Rp.", gaji)
    print("Potongan Pajak    : Rp.", pph(gaji))
    print("Tunjangan Jabatan : Rp.", tunjangan(jabatan, gaji))
    
    total_gaji = gaji - pph(gaji) + tunjangan(jabatan, gaji)
    print("Total Gaji Bersih : Rp.", total_gaji)


def pph(gaji):
    pph = gaji * 0.05 
    return pph


def tunjangan(jabatan, gaji):
    if jabatan == "manager":
        return gaji * 0.10   # Tunjangan 10%
    elif jabatan == "staff":
        return gaji * 0.05   # Tunjangan 5%
    else:
        return 0


# Input data dari user
nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (manager/staff): ").lower()
gaji = int(input("Masukkan gaji pokok: "))

identitas(nama, jabatan, gaji)