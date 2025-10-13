 # Soal 3 - Parkir Mall

# lama = float(input("Masukkan lama parkir (jam): "))
# vip = input("Apakah member VIP? (ya/tidak): ")

# if vip == "ya":  #jika vip maka biaya nya 0
#     biaya = 0
# else:
#         if lama <= 2:
#             biaya = 5000  #jika biaya lama nya 2 ja pertama biaya 5000
#         else:
#             biaya = 5000 + (lama - 2) * 3000  #biaya bertambah 3000 setiap jam nya
#         if biaya > 20000:
#             biaya = 20000  #maksimal biaya per hari nya 20000

# print(f"Total biaya parkir: Rp {int(biaya)}")

lama = float(input("Masukkan lama parkir (jam): "))
vip = input("Apakah member VIP? (ya/tidak): ")

if vip == "ya":
    biaya = 0
else:
    # Hitung jumlah hari penuh dan sisa jam
    hari = lama // 24        # jumlah hari penuh
    sisa_jam = lama % 24          # sisa jam setelah hari penuh

    # Biaya untuk hari penuh
    biaya = hari * 20000          # setiap hari penuh dihitung 20.000

    # Biaya untuk sisa jam (hari terakhir)
    if sisa_jam == 0 :
        biaya += 0
    elif sisa_jam <= 2:
        biaya += 5000
    else:
        biaya += 5000 + (sisa_jam - 2) * 3000
        
        # Batas harian tetap 20.000
    if biaya - hari * 20000 > 20000:
        biaya = hari * 20000 + 20000

print(f"Total biaya parkir: Rp {int(biaya)}")


