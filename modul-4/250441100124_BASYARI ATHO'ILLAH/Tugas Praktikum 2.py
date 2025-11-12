gaji_pokok = 100000
lembur_per_jam = 25000

total_gaji = 0
total_lembur = 0
total_bonus = 0

print("=== Program Hitung Gaji Mingguan Pak Wowo ===\n")

for i in range(1, 8):  # 7 hari kerja

    
    lembur = int(input(f"Masukkan jam lembur hari ke-{i}: "))
        
    if lembur == 0:
        gaji_lembur = 0
    elif lembur < 4:
        gaji_lembur = lembur_per_jam * lembur
    elif lembur == 4:
        gaji_lembur = 100000
    elif lembur == 5:
        gaji_lembur = 125000
    elif lembur == 6:
        gaji_lembur = 200000
    elif lembur == 7:
        gaji_lembur = 225000
    elif lembur == 8:
        gaji_lembur = 300000
    else:
        print("Lembur melebihi batas, tidak dihitung.")
        gaji_lembur = 0
        lembur = 0 

    shift = input("Apakah shift malam? (y/n): ").lower()
    if shift == "y":
        bonus = 50000
    else:
        bonus = 0

    total_gaji += gaji_pokok + gaji_lembur + bonus
    total_lembur += lembur
    total_bonus += bonus

print("=== Rekap Gaji Mingguan ===")
print(f"Total jam lembur selama: {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus}")
print(f"Total gaji selama seminggu: Rp{total_gaji}")
