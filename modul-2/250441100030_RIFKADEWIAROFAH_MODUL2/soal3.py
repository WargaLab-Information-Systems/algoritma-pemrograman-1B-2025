parkir = int(input("Masukkan total jam parkir: "))
vip = input("Apakah anda member VIP? (ya/tidak): ")

if vip == "ya":
    biaya = 0
else:
    if parkir <= 2:
        biaya = 5000
    else:
        biaya = 5000 + (parkir-2) * 3000
    if biaya > 20000:
        biaya = 20000
print("Total biaya parkir: Rp", biaya)  