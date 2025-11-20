gaji_pokok = 100000
total_gaji = 0
total_lembur = 0
total_bonus = 0
gaji_lembur2 = 0
for hari in range(1, 8):
    print(f"Hari ke-{hari}")

    jam_lembur = int(input("Masukkan jumlah jam lembur: "))
    shift_malam = input("Apakah hari ini termasuk shift malam? (y/n): ")
    
    if jam_lembur < 0:
        print("Input tidak valid, ulangi hari ini.")
        continue
    if jam_lembur <= 5:
        gaji_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        gaji_lembur = 100000
    elif jam_lembur == 6:
        gaji_lembur = 200000
    elif jam_lembur == 7:
        gaji_lembur = 250000
    elif jam_lembur == 8 :
        gaji_lembur = 300000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        gaji_lembur = 300000
    else:
        gaji_lembur = 0
    
    if shift_malam == "y":
        bonus_malam = 50000 
    else :
        bonus_malam = 0
    gaji_harian = gaji_pokok + gaji_lembur + bonus_malam
    gaji_lembur2 += gaji_lembur
    total_gaji += gaji_harian
    total_lembur += jam_lembur
    total_bonus += bonus_malam
    

print(f"Total jam lembur: {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus}")
print(f"Total gaji dari jam lembur : Rp{gaji_lembur2}")
print(f"Total gaji seminggu: Rp{total_gaji}")
