# input lama parkir,status VIP
lama_parkir_jam = int(input("masukkan lama parkir(jam): "))
status_vip = input("apakah anda member vip? (ya/tidak): ")
# tambahan biaya parkir setelah 2 jam pertama
biaya = 3000
total_biaya_parkir = 0
# cek status VIP
if status_vip == "ya":
    total_biaya_parkir = 0
else:
    if lama_parkir_jam <= 2:
        total_biaya_parkir = 5000
    else:
        total_biaya_parkir = 5000 + (lama_parkir_jam - 2) * biaya 
# batas maksimal tarif per hari
if total_biaya_parkir > 20000:
    total_biaya_parkir = 20000
# cetak total biaya parkir
print("total biaya parkir : Rp",total_biaya_parkir)