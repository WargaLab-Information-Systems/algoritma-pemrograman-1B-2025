total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")
    jam = int(input("Masukkan jumlah jam lembur: "))
    shift = input("Apakah shift malam? (y/n): ")

    gaji_pokok = 100_000
    lembur = 0
    bonus = 50_000 if shift == 'y' else 0

    # Hitung lembur sesuai aturan
    if jam > 8:
        print("Lembur melebihi batas, tidak dihitung.")
    elif jam == 8:
        lembur = 300_000
    elif jam == 6:
        lembur = 200_000
    elif jam == 4:
        lembur = 100_000
    elif 1 <= jam <= 3:
        lembur = jam * 25_000

    gaji_harian = gaji_pokok + lembur + bonus

    total_gaji += gaji_harian
    total_lembur += lembur
    total_bonus += bonus

print(f"Total lembur: Rp{total_lembur}")
print(f"Total bonus shift malam: Rp{total_bonus}")
print(f"Total gaji seminggu: Rp{total_gaji}")
