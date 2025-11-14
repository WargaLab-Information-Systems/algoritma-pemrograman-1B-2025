print("Program Hitung Gaji Mingguan")

total_gaji = 0
total_lembur = 0
total_bonus_shift = 0
total_upah_lembur = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")
    shift_malam = input("Apakah shift malam? (y/n): ")
    if shift_malam == "y":
        jam_lembur = int(input("Masukkan jam lembur: "))
    else:
        jam_lembur = 0

    gaji_pokok = 100000
    bonus_shift = 0
    upah_lembur = 0
    if jam_lembur == 0:
        upah_lembur = 0
    elif jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 5:
        upah_lembur = 125000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 7:
        upah_lembur = 225000
    elif jam_lembur == 8:
        upah_lembur = 300000
    else:
        print("Jam lembur melebihi batas, tidak dihitung.")
        upah_lembur = 300000

    if shift_malam == "y":
        bonus_shift = 50000

    total_gaji += gaji_pokok + bonus_shift + upah_lembur
    total_lembur += jam_lembur
    total_bonus_shift += bonus_shift
    total_upah_lembur += upah_lembur
    gaji_pokok = gaji_pokok * 7

print("=== Rekap Gaji Mingguan ===")
print("Total jam lembur:", total_lembur, "jam")
print("Total upah lembur: Rp", total_upah_lembur)
print("Total bonus shift malam: Rp", total_bonus_shift)
print("Total gaji pokok: Rp", gaji_pokok)
print("--------------------------------")
print("Total gaji selama seminggu: Rp", total_gaji)