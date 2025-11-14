nama_karyawan = input("Masukkan nama Karyawan : ")
jabatan_karyawan = input("Masukkan Jabatan Karyawan (Staff/Manager) : ")
gaji_pokok = float(input("Masukkan Gaji Pokok Karyawan : "))

def hitung_gaji_bersih():
    pajak = gaji_pokok * 5 / 100


    if jabatan_karyawan == "Manager" or jabatan_karyawan == "manager":
        tunjangan = gaji_pokok * 0.1
    elif jabatan_karyawan == "Staff" or jabatan_karyawan == "staff":
        tunjangan = gaji_pokok * 0.05
    else:
        
        tunjangan = 0

    gaji_bersih = gaji_pokok - pajak + tunjangan

    print("\n RINCIAN GAJI KARYAWAN ")
    print("=" * 30)
    print(f"Nama Karyawan : {nama_karyawan}")
    print(f"Jabatan       : {jabatan_karyawan}")
    print("-" * 30)
    print(f"Gaji Pokok    : Rp{int(gaji_pokok)}")
    print(f"Tunjangan (+) : Rp{int(tunjangan)}")
    print(f"Pajak 5%  (-) : Rp{int(pajak)}")
    print("-" * 30)
    print(f"Total Gaji Bersih: Rp{int(gaji_bersih)}")


hitung_gaji_bersih()