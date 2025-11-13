t_gaji = 0
t_lembur = 0
t_bonus = 0

for hari in range(1, 8):
    print(f"hari ke-{hari}:")

    jam = (input("masukkan jumlah jam lembur:"))
    while not all(c in "0123456789" for c in jam):
        print("masukkan angka aja")
        jam = input("masukkan jumlah jam lembur:")
    jam = int(jam)

    shift = input("apakah shift malam?(y/n):")
    while shift not in ["y", "n"]:
        print("masukkan y atau n aja")
        shift = input("apakah shift malam? (y/n)")

    gaji_pokok = 100000
    uang_lembur = 0
    bonus_shift = 0

    if 1 <= jam <= 3:
        uang_lembur = jam * 25000
    elif jam == 4:
        uang_lembur = 100000
    elif jam == 6:
        uang_lembur = 200000
    elif jam == 8:
        uang_lembur = 300000
    elif jam > 8:
        print("lembur lebih dari batas tidak dihitung")
        jam = 0

    if shift == "y":
        bonus_shift = 50000

    gaji_harian = gaji_pokok + uang_lembur + bonus_shift
    
    t_gaji += gaji_harian
    t_lembur += jam
    t_bonus += bonus_shift
    print(f"gaji hari ke-{hari}: rp{gaji_harian}")

print("==== rekap gaji miingguan ====")
print(f"total jam lembur : {t_lembur} jam")
print(f"total bonus shift malam: Rp{t_bonus}")
print(f"total gaji selama seminggu: Rp{t_gaji}")