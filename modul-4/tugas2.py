print("=== Program Gaji Mingguan Pak Wowo ===")

total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print("\nHari ke-", hari)

    # Input jam lembur (tanpa strip)
    while True:
        jam_input = input("Masukkan jumlah jam lembur: ")
        if jam_input == "":
            print("Tidak boleh kosong! Masukkan angka.")
            continue

        hanya_angka = True
        for c in jam_input:
            if c not in "0123456789":
                hanya_angka = False
                break

        if hanya_angka:
            jam = int(jam_input)
            break
        else:
            print("Input tidak valid! Masukkan angka saja.")

    # Input shift malam (tanpa strip)
    while True:
        shift = input("Apakah shift malam? (y/n): ")
        if shift == "y" or shift == "n" or shift == "Y" or shift == "N":
            break
        else:
            print("Input tidak valid! Ketik y untuk ya atau n untuk tidak.")

    # Hitung gaji harian
    gaji = 100000
    bonus_lembur = 0

    if jam > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam = 0
    elif jam >= 1 and jam <= 3:
        bonus_lembur = jam * 25000
    elif jam == 4:
        bonus_lembur = 100000
    elif jam == 5 :
        bonus_lembur = jam * 25000
    elif jam == 6:
        bonus_lembur = 200000
    elif jam == 7 :
        bonus_lembur = jam * 25000
    elif jam == 8:
        bonus_lembur = 300000

    bonus_shift = 0
    if shift == "y" or shift == "Y":
        bonus_shift = 50000

    total_gaji = total_gaji + gaji + bonus_lembur + bonus_shift
    total_lembur = total_lembur + jam
    total_bonus = total_bonus + bonus_shift

print("\n=== Rekap Mingguan ===")
print("Total jam lembur :", total_lembur, "jam")
print("Total bonus shift malam: Rp", total_bonus)
print("Total gaji seminggu   : Rp", total_gaji)
