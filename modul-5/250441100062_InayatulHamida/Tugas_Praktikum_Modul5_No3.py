def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    pajak = gaji_pokok * 0.05
    
    if jabatan == "manager":
        tunjangan = gaji_pokok * 0.10
    elif jabatan == "staff":
        tunjangan = gaji_pokok * 0.05
    else:
        tunjangan = 0  

    gaji_bersih = gaji_pokok + tunjangan - pajak

    print(f"Nama Karyawan: {nama}")
    print(f"Jabatan: {jabatan}")
    print(f"Gaji Pokok: {gaji_pokok}")
    print(f"Tunjangan: {tunjangan}")
    print(f"Pajak: {pajak}")
    print(f"Gaji Bersih: {gaji_bersih}")

nama_karyawan = input("Masukkan nama karyawan: ")
jabatan_karyawan = input("Masukkan jabatan karyawan (Manager/Staff): ")
gaji_pokok_karyawan = float(input("Masukkan gaji pokok karyawan: "))

hitung_gaji_bersih(nama_karyawan, jabatan_karyawan, gaji_pokok_karyawan)