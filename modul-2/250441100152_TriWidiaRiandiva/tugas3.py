# Menghitung tarif parkir mall

tarif_awal = 5000
tarif_per_jam_selanjutnya = 3000
tarif_maksimal = 20000

lama_parkir = int(input("Masukkan lama parkir (jam): "))
status_vip = input("Apakah Anda member VIP? (ya/tidak): ")

biaya = 0
if status_vip == "ya":
    biaya = 0
else :
    if lama_parkir <= 2:
        biaya = tarif_awal
    else:
        biaya = tarif_awal + (lama_parkir - 2) * tarif_per_jam_selanjutnya
if biaya > tarif_maksimal:
    biaya = tarif_maksimal

print("Total biaya parkir: Rp", biaya)
