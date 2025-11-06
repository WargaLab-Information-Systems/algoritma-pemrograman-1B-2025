total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}:")
    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur (0–8): "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif.")
                continue
            elif jam_lembur > 8:
                print("Lembur melebihi batas, tidak dihitung.")
                jam_lembur = 0
            break
        except ValueError:
            print("Input tidak valid. Harus berupa angka.")
    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").strip().lower()
        if shift_malam in ["y", "n"]:
            break
        else:
            print("Input tidak valid. Masukkan 'y' atau 'n'.")

    gaji_pokok = 100_000
    bonus_shift = 50_000 if shift_malam == "y" else 0

    if 1 <= jam_lembur <= 3:
        gaji_lembur = jam_lembur * 25_000
    elif jam_lembur == 4:
        gaji_lembur = 100_000
    elif jam_lembur == 6:
        gaji_lembur = 200_000
    elif jam_lembur == 8:
        gaji_lembur = 300_000
    else:
        gaji_lembur = 0

    total_harian = gaji_pokok + gaji_lembur + bonus_shift
    total_gaji += total_harian
    total_lembur += jam_lembur
    total_bonus += bonus_shift

print("\n=== Rekap Gaji Mingguan Pak Wowo ===")
print(f"Total jam lembur        : {total_lembur} jam")
print(f"Total bonus shift malam : Rp{total_bonus:,}")
print(f"Total gaji seminggu     : Rp{total_gaji:,}")
