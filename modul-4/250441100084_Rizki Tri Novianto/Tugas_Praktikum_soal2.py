total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print("Hari ke-", hari)

    # Input jam lembur
    while True:
        jam = input("Jam lembur (1-8): ")
        if len(jam) > 0 and all('0' <= c <= '9' for c in jam):
            jam = int(jam)
            break
        print("Input tidak valid.")

        
    # Input shift malam
    while True:
       
        shift = input("Shift malam? (y/n): ")
        if shift == 'y' or shift == 'n':
            break
        print("Input harus 'y' atau 'n'.")


    gaji = 100000
    if 1 <= jam <= 3:
        gaji = gaji+ jam * 25000
        total_lembur = total_lembur + jam
    elif jam == 4:
        gaji += 100000
        total_lembur += jam
    elif jam == 6:
        gaji += 200000
        total_lembur += jam
    elif jam == 8:
        gaji += 300000
        total_lembur += jam
    elif jam > 8:
        print("Lembur melebihi batas, tidak dihitung.")

    if shift == 'y':
        gaji += 50000
        total_bonus += 50000

    total_gaji += gaji
    print(f"Gaji hari ke- {hari} : {gaji}")
    print("-----------------------------")

print("Total jam lembur:", total_lembur)
print("Total bonus shift malam:", total_bonus)
print("Total gaji seminggu:", total_gaji)