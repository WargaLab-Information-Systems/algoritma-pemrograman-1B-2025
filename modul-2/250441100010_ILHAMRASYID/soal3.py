jam_parkir = int(input("masukkan lama parkir : "))
vip = input("apakah member vip? (ya/tidak) : ")

if vip == "ya":
    biaya = 0
else:
    if jam_parkir <= 2:
        biaya = 5000
    else:
        biaya = 5000 + (jam_parkir - 2) * 3000
    if biaya > 20000:
        biaya = 20000

print("total biaya parkir: Rp", biaya)