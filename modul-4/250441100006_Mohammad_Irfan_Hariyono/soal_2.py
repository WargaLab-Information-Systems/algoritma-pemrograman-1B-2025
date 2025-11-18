print(" Program Menghitung Gaji Mingguan Pak Wowo")

total_gaji_mingguan = 0
total_jam_lembur = 0
total_bonus_malam = 0

gaji_pokok = 100000
bonus_malam = 50000
jumlah_hari = 7

for hari in range (1, jumlah_hari + 1):
    print(f"\n Hari ke-{hari}")

    gaji_harian = gaji_pokok
    bonus_lembur_harian = 0
    bonus_malam_harian = 0

    while True:
        shift_malam = input(f"Apakah hari ke-{hari} shift malam (iya/tidak): ")
        pass

        if shift_malam == "iya" or shift_malam == "tidak":
            break
        else:
            print("Error : Input harus 'iya' atau 'tidak'. Coba lagi yaa")

    while True:
        jam_lembur = input(f"Masukkan jam lembur hari ke-{hari}: ")

        input_angka_valid = True

        if jam_lembur == "":
            input_angka_valid = False
        elif jam_lembur == 0:
            input_angka_valid == False
        else:
            for karakter in jam_lembur:
                if karakter not in "0123456789":
                    input_angka_valid = False
                    break
        if input_angka_valid:
            jam_lembur = int(jam_lembur)
            break
        else:
            print("Error : Input harus berupa angka bulat positif ( 1, 2, 3 ...). Coba inputkan lagi.")

    if jam_lembur > 8 :
        print("Peringatan : Lembur melebihi batas (8 jam), bonus lembur tidak dihitung.")
        bonus_lembur_harian = 0
    elif jam_lembur == 8:
        bonus_lembur_harian = 300000
    elif jam_lembur == 6:
        bonus_lembur_harian = 200000
    elif jam_lembur == 4:
        bonus_lembur_harian = 100000
    elif 1 <= jam_lembur <= 3:
        bonus_lembur_harian = jam_lembur * 25000

    if shift_malam == "iya":
        bonus_malam_harian = bonus_malam

    total_jam_lembur += jam_lembur
    total_bonus_malam += bonus_malam_harian
    gaji_harian = gaji_pokok + bonus_lembur_harian + bonus_malam_harian
    total_gaji_mingguan += gaji_harian
print("\n ========================================== ")
print("                 Rekapitulasi                 ")
print("\n ========================================== ")
print(f"Total Jam lembur pak wowo seminggu: {total_jam_lembur} jam")
print(f"Total Bonus pak wowo shift malam: Rp{total_bonus_malam}")
print(f"Total Gaji mingguan pak wowo:     Rp{total_gaji_mingguan}")
print("x" * 35)