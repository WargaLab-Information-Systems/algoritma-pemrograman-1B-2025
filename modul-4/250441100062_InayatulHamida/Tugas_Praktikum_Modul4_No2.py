gaji_pokok = 100000
total_gaji = 0
total_jam_lembur = 0
total_bonus_malam = 0
total_bonus_dalam_seminggu = 0

for hari in range(1, 8):
    while True:
        try:
            jam_lembur = int(input(f"Hari ke-{hari}: Masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif. Coba lagi.")
                continue
            
            shift_malam = input("Apakah hari ini shift malam? (y/n): ")
            if shift_malam not in ['y', 'n']:
                print("Input tidak valid. Harus 'y' atau 'n'. Coba lagi.")
                continue
            
            break 

        except ValueError:
            print("Input tidak valid. Masukkan angka untuk jam lembur. Coba lagi.")

    if jam_lembur < 5:
        gaji_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        gaji_lembur = 100000
    elif jam_lembur == 6:
        gaji_lembur = 200000
    elif jam_lembur == 8:
        gaji_lembur = 300000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        gaji_lembur = 0
    else:
        gaji_lembur = 0

    if shift_malam == 'y':
        bonus_malam = 50000
        total_bonus_malam += bonus_malam
    else:
        bonus_malam = 0

    total_hari_gaji = gaji_pokok + gaji_lembur + bonus_malam
    total_gaji += total_hari_gaji
    total_jam_lembur += jam_lembur
    total_bonus_dalam_seminggu += gaji_lembur

print(f"\nTotal jam lembur: {total_jam_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus_malam}")
print(f"Total gaji seminggu: Rp{total_gaji}")
print(f"Total gaji bonus dalam seminggu: Rp{total_bonus_dalam_seminggu}")