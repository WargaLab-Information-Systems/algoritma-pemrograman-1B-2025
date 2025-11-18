total_gaji = 0
total_lembur_jam = 0
total_bonus_malam = 0
total_biaya_lembur = 0
gaji_pokok = 100000

print("gaji pokok per hari adalah Rp100000")
print("Program perhitungan gaji karyawan selama 7 hari")
print("===============================================")
print()

for hari in range(1, 8):
    while True:
        shift_malam = input(f"Hari {hari}: Apakah hari ini anda shift malam? (y/n): ")
        if shift_malam == "y":
            bonus_malam = 50000
            print(f"Anda mendapatkan bonus shift malam sebesar Rp{bonus_malam}")
            break
        elif shift_malam == "n":
            bonus_malam = 0
            print("Tidak ada bonus shift malam hari ini.")
            break

    while shift_malam == "y" or shift_malam == "n":
        lembur = input("Apakah anda lembur hari ini? (y/n): ")
        if lembur == "y":
            break
        elif lembur == "n":
            jam_lembur = 0
            bayaran_lembur = 0
            print("Tidak ada bayaran lembur hari ini.")
            print()
            break

    while lembur == "y":
        jam_lembur = int(input(f"Masukkan jumlah jam lembur: "))
        if jam_lembur == 0:
            bayaran_lembur = 0
            print("Tidak ada bayaran lembur hari ini.")
            print()
            break
        elif 1 <= jam_lembur <= 3:
            bayaran_lembur = 25000 * jam_lembur
            print(f"Bayaran lembur untuk {jam_lembur} jam adalah Rp{bayaran_lembur}")
            print()
            break
        elif jam_lembur == 4:
            bayaran_lembur = 100000
            print(f"Bayaran lembur untuk {jam_lembur} jam adalah Rp{bayaran_lembur}")
            print()
            break
        elif jam_lembur == 5:
            bayaran_lembur = 125000
            print(f"Bayaran lembur untuk {jam_lembur} jam belum diatur dalam sistem.")
            print()
            break
        elif jam_lembur == 6:
            bayaran_lembur = 200000
            print(f"Bayaran lembur untuk {jam_lembur} jam adalah Rp{bayaran_lembur}")
            print()
            break
        elif jam_lembur == 7:
            bayaran_lembur = 225000
            print(f"Bayaran lembur untuk {jam_lembur} jam belum diatur dalam sistem.")
            print()
            break
        elif jam_lembur == 8:
            bayaran_lembur = 300000
            print(f"Bayaran lembur untuk {jam_lembur} jam adalah Rp{bayaran_lembur}")
            print()
            break
        else:
            bayaran_lembur = 0  
            print("lembur melebihi batas, tidak dihitung")
            print()
            break

    gaji_hari = gaji_pokok + bayaran_lembur + bonus_malam
    total_gaji += gaji_hari
    total_lembur_jam = total_lembur_jam + jam_lembur
    total_biaya_lembur += bayaran_lembur
    total_bonus_malam += bonus_malam  

print()
print("===============================================")
print(f"Total jam lembur: {total_lembur_jam}")
print(f"Total bayaran lembur: Rp{total_biaya_lembur}")
print(f"Total bonus shift malam: Rp{total_bonus_malam}")
print(f"Gaji pokok selama 7 hari: Rp{gaji_pokok * 7}")
print(f"Total gaji seminggu: Rp{total_gaji}")
