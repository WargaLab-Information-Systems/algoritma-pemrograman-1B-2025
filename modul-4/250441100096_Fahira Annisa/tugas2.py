total_lembur = 0
total_bonus = 0
total_gaji = 0

for i in range(1, 8):
    print(f"\n hari ke-{i}")
    while True: 
         jam = int(input("Masukkan jam lembur: "))
         if 0 <= jam <= 8:
          break

    while True:
        shift = input("shift malam? (iya/tidak):").lower()
        if shift in ["iya", "tidak"]:
            break
        else:
           print("input tidak valid. Masukkan 'iya' atau 'tidak'. ")
    gaji = 100000 # Rp.100.000
    if 1 <= jam <= 3:
        lembur = jam * 25000 # Rp.25.000
    elif jam == 4:
        lembur = 100000 # Rp.100.000
    elif jam == 6:
        lembur = 200000 # Rp.200.000
    elif jam == 8:
        lembur = 300000 # Rp.300.000
    elif jam > 8:
        print("Lembur melebihi batas")
        lembur = 0
    else:
        lembur = 0
    
    bonus = 50000 
    total_gaji += gaji + lembur
    total_lembur += jam

if shift == "iya":
    total_gaji += bonus
    total_bonus += bonus


print("\n=== Total Mingguan===")
print("Total jam lembur:", total_lembur)
print("Total bonus: Rp", total_bonus)
print("Total gaji: Rp", total_gaji)

