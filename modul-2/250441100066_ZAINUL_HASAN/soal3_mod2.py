jam_parkir = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah member VIP? (ya/tidak): ")

if vip == "ya":
    biaya = 0
else:
    if jam_parkir <= 2:
        biaya = 5000
    elif jam_parkir <= 24:
        biaya = 5000 + (jam_parkir - 2) * 3000
        if biaya > 20000:
            biaya = 20000
    else :
        jam_parkir = jam_parkir - 24
        biaya = 25000 + (jam_parkir - 2) * 3000
print("Total biaya parkir: Rp", biaya)