lama_parkir = int(input("Masukkan lama parkir (jam):"))

status_vip = input("Apakah member VIP? (ya/tidak) :")

biaya = 0

if status_vip == "ya":
    biaya = 0
else:
    if lama_parkir <= 2:
        biaya = 5000
    else: 
        biaya = 5000 + (lama_parkir - 2) * 3000
    
    if biaya > 20000:
        biaya = 20000

print(f"Total biaya parkir: Rp {biaya:}") 

