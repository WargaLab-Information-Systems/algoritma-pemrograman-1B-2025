#soal nomer 3

lama_parkir = int(input("Masukkan lama parkir (jam): "))
status_vip = input("Apakah member VIP? (ya/tidak): ")


tarif_awal = 5000          
tarif_per_jam = 3000       
maksimal_tarif_harian = 20000  

#penyeleksian
if status_vip == "ya":
    total = 0
else:
    hari = lama_parkir // 24 #jumlah hari penuh
    sisa_jam = lama_parkir % 24 #sisa jam setelah sehari penuh

    total = hari * maksimal_tarif_harian
#biaya untuk sisa jam hari terakhir
    if sisa_jam == 0 :
        total += 0 
    elif sisa_jam <= 2:
        total += tarif_awal
    else:
        total += tarif_awal + (sisa_jam - 2) * tarif_per_jam
#batas harian tetap pada 20000
    if total - hari * maksimal_tarif_harian > maksimal_tarif_harian:
        total = hari  * maksimal_tarif_harian + maksimal_tarif_harian
    

print()
print("Total biaya parkir: Rp.", total)