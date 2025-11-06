# Input dari pengguna
nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan (Manager/Staff): ")
gaji_pokoknya = float(input("Masukkan gaji pokok: "))

def hitung_gaji_bersih():
    # Hitung pajak 5% dari gaji pokok
    pajak = gaji_pokoknya * 5 / 100

    # hitung dari jabatan yang di masukkan
    if jabatan == "Manager" or "manager":
        tunjangan = gaji_pokoknya * 10 // 100
    elif jabatan == "Staff" or "staff":
        tunjangan =  gaji_pokoknya * 5 // 100
    else:
        # untuk jabatan yang tidak di kenal
        tunjangan = 0 


    gaji_bersih = gaji_pokoknya - pajak + tunjangan


    print("=== Rincian Gaji ===")
    print(f"Nama       : {nama}")
    print(f"Jabatan    : {jabatan}")
    print(f"Gaji Pokok : {int(gaji_pokoknya)}")
    print(f"Pajak 5%   : {int(pajak)}")
    print(f"Tunjangan  : {int(tunjangan)}")
    print(f"Gaji Bersih: {int(gaji_bersih)}")


hitung_gaji_bersih()