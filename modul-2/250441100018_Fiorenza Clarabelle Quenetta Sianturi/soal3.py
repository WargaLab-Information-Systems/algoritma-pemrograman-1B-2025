lama_parkir = int(input("Masukkan lama parkir (dalam jam): "))
vip = input("Apakah Anda member VIP? (ya/tidak): ")

tarif_2jam = 5000
tarif_selanjutnya = 3000

if vip == "ya":
    total_biaya = 0
elif lama_parkir <= 2:
    total_biaya = tarif_2jam
elif lama_parkir <= 7:
    total_biaya = tarif_2jam + ((lama_parkir - 2) * tarif_selanjutnya) 
else: 
    total_biaya = 20000

print(f"Total biaya parkir: {total_biaya}")