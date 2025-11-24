# Program menghitung total gaji mingguan Pak Wowo2

total_gaji = 0
total_bonus = 0
total_lembur = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")
    try:
        jam_lembur = int(input("Masukkan jumlah jam lembur: "))
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
    except:
        print("Input tidak valid, coba lagi.")
        continue

    gaji_pokok = 100000
    gaji_harian = gaji_pokok

    # Hitung lembur
    if 1 <= jam_lembur <= 3:
        gaji_harian += jam_lembur * 25000
        total_lembur += jam_lembur * 25000
    elif jam_lembur == 4:
        gaji_harian += 100000
        total_lembur += 100000
    elif jam_lembur == 6:
        gaji_harian += 200000
        total_lembur += 200000
    elif jam_lembur == 8:
        gaji_harian += 300000
        total_lembur += 300000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")

    # Bonus shift malam
    if shift_malam == "y":
        gaji_harian += 50000
        total_bonus += 50000

    total_gaji += gaji_harian

print("\n=== Rekapitulasi Mingguan ===")
print(f"Total lembur   : Rp{total_lembur}")
print(f"Total bonus    : Rp{total_bonus}")
print(f"Total gaji 7 hari: Rp{total_gaji}")