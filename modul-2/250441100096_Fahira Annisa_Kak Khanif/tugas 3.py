tarif_awal = 5000
tarif_per_jam = 3000
tarif_maksimal = 20000

lama_parkir = int(input("Masukkan berapa jam kamu parkir: "))
vip = input("Apakah kamu termasuk anggota VIP? (ya/tidak): ")

if vip == "iya":
    biaya = 0
else:
    if lama_parkir <= 2:
        biaya = tarif_awal
    else:
        hari = lama_parkir // 24 
        sisa_jam = lama_parkir % 24
        total = hari * tarif_maksimal

        if sisa_jam == 0:
            total += 0
        elif sisa_jam <= 2:
            total += tarif_awal
        else:
            total += tarif_awal + (sisa_jam - 2) * tarif_per_jam

        if total - hari * tarif_maksimal > tarif_maksimal:
            total = hari * tarif_maksimal + tarif_maksimal

print()
print("total biaya parkir: Rp.", total)