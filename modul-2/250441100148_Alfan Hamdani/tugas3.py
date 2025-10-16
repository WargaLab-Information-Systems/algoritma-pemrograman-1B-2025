# Program hitung biaya parkir di Mall
lama_parkir = int(input("Masukkan lama parkir (jam): "))
status_vip = input("Apakah Anda member VIP? (ya/tidak): ")

# proses
if status_vip == "ya":
    total_biaya = 0
else:
    if lama_parkir <= 2:
        total_biaya = 5000
    else:
        total_biaya = 5000 + (lama_parkir - 2) * 3000

# Maksimal parkir per hari
if total_biaya > 20000:
    total_biaya = 20000

print("Total biaya parkir: Rp.", total_biaya)