total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    jam = int(input(f"Masukkan jam lembur hari ke-{hari}: "))
    malam = input("Shift malam? (y/n): ").lower()

    if jam > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur = 0
    elif 1 <= jam <= 3:
        lembur = jam * 25000
    elif jam == 4:
        lembur = 100000
    elif jam == 6:
        lembur = 200000
    elif jam == 8:
        lembur = 300000
    else:
        lembur = 0

    bonus = 50000 if malam == "y" else 0
    gaji_harian = 100000 + lembur + bonus

    total_gaji += gaji_harian
    total_lembur += lembur
    total_bonus += bonus

print("\nTotal lembur:", total_lembur)
print("Total bonus:", total_bonus)
print("Total gaji seminggu:", total_gaji)