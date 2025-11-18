def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok #5%
    if jabatan == "manager":
        tunjangan = 0.10 * gaji_pokok #10%
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok #5%
    else:
        tunjangan = 0
    gaji_bersih = gaji_pokok - pajak + tunjangan
    return gaji_bersih

nama = input("masukkan nama karyawan: ")
if nama != "0123456789" :
    print("nama tidak boleh angka, hanya berupa huruf, mohon masukkan kembali")
    nama = input("masukkan nama karyawan: ")
  
jabatan = input("masukkan jabatan (manager/staff): ").lower()


gaji_pokok = float(input("masukkan gaji pokok: "))
if gaji_pokok < 0:
    print("hanya masukkan bialangan positif, mohon masukkan kembali")
    gaji_pokok = float(input("masukkan gaji pokok: "))
hasil = hitung_gaji(nama, jabatan, gaji_pokok)
print(f"gaji bersih {nama} sebagai {jabatan} adalah Rp{hasil}")