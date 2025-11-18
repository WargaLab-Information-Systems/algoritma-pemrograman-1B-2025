total_gaji = 0
total_lembur = 0
total_bonus_shift_malam = 0

print("=== Program Perhitungan Gaji Mingguan Pak Wowo ===")

for hari in range(1, 8):
    print("Hari ke-",hari)
    
    # Input jam lembur 
    while True:
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            if 0 <= jam_lembur <= 8:
                break
            elif jam_lembur > 8:
                print("Lembur melebihi batas, tidak dihitung.")
                jam_lembur = 0
                break

    # Input shift malam 
    while True:
        shift_malam = input("apakah shift malam? (y/n): ") 
        if shift_malam in ["y" , "n"]:
            break
        else:
             print("input tidak valid, masukkan y / n") 


    # Hitung gaji harian
    gaji_harian = 100000  # Gaji pokok
    if 1 <= jam_lembur <= 3:
        gaji_harian += jam_lembur * 25000
    elif jam_lembur == 4:
        gaji_harian += 100000
    elif jam_lembur == 5:
        gaji_harian += 25000
    elif jam_lembur == 6:
        gaji_harian += 200000
    elif jam_lembur == 7:
        gaji_harian += 25000
    elif jam_lembur == 8:
        gaji_harian += 300000
# Tambahkan bonus shift malam
    if shift_malam == 'y':
        gaji_harian += 50_000
        total_bonus_shift_malam += 50000

    total_gaji += gaji_harian
    total_lembur += jam_lembur

# Tampilkan hasil akhir
print("Total jam lembur: ",total_lembur, "jam")
print("Total bonus shift malam: Rp",total_bonus_shift_malam)
print("Total gaji seminggu: Rp",total_gaji)

    
    