total_gaji = 0
total_lembur = 0
total_bonus = 0
bonus_lembur = 0

for hari in range(1, 8):
    print("Hari ke-", hari)
    
    jam_lembur = int(input("Masukkan jumlah jam lembur: "))
    shift_malam = input("Apakah shift malam? (y/n): ")
    
    gaji_pokok = 100000
    tambahan_lembur = 0
    bonus_shift = 0
    
    if jam_lembur == 0:
        tambahan_lembur = 0
    elif 1 <= jam_lembur <= 3:
        tambahan_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        tambahan_lembur = 100000
    elif jam_lembur == 6:
        tambahan_lembur = 200000
    elif jam_lembur == 8:
        tambahan_lembur = 300000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        tambahan_lembur = 0
    
    if shift_malam == "y":
        bonus_shift = 50000
    
    total_gaji += gaji_pokok + tambahan_lembur + bonus_shift
    total_lembur += jam_lembur
    total_bonus += bonus_shift
    bonus_lembur += tambahan_lembur
    gaji_pokok = gaji_pokok * 7

print("=== Rekap Gaji Mingguan ===")
print("Total jam lembur:", total_lembur, "jam")
print("Total Bonus Lembur", bonus_lembur)
print("Total bonus shift malam: Rp", total_bonus)
print("Total Gaji Pokok", gaji_pokok)
print("Total gaji seminggu: Rp", total_gaji)