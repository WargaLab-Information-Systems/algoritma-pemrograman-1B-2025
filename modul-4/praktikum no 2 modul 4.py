gaji_pokok_harian = 100000
total_gaji = 0
total_jam_lembur = 0
total_bonus_shift = 0

for hari in range(1, 8):
    print(f"\n        Hari ke-{hari}      ")
    
    shift_malam = input("Apakah hari ini shift malam? (y/n): ")
    
    if shift_malam == 'y':
        jam_lembur = int(input("Masukkan jumlah jam lembur: "))
    else:
        jam_lembur = 0
    
    gaji_hari_ini = gaji_pokok_harian

    if shift_malam == 'y':
        if jam_lembur > 8:
            print("Lembur melebihi batas, tidak dihitung.")
            uang_lembur = 0
        elif jam_lembur == 8:
            uang_lembur = 300000
            total_jam_lembur += jam_lembur
        elif jam_lembur == 6:
            uang_lembur = 200000
            total_jam_lembur += jam_lembur
        elif jam_lembur == 4:
            uang_lembur = 100000
            total_jam_lembur += jam_lembur
        elif jam_lembur == 3:
            uang_lembur = jam_lembur * 25000
            total_jam_lembur += jam_lembur
        elif jam_lembur == 2:
            uang_lembur = jam_lembur * 25000
            total_jam_lembur += jam_lembur
        elif jam_lembur == 1:
            uang_lembur = jam_lembur * 25000
            total_jam_lembur += jam_lembur
        else:
            uang_lembur = jam_lembur * 25000
            if jam_lembur > 0:
                total_jam_lembur += jam_lembur
        
        gaji_hari_ini += uang_lembur

        bonus_shift = 50000
        gaji_hari_ini += bonus_shift
        total_bonus_shift += bonus_shift
    else:
        uang_lembur = 0
    
    total_gaji += gaji_hari_ini
    print(f"Gaji hari ke-{hari}: Rp{gaji_hari_ini:,}")

print(f"Total jam lembur: {total_jam_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus_shift:,}")
print(f"Total gaji seminggu: Rp{total_gaji:,}")
