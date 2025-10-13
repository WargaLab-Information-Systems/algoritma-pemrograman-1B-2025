# Hitung biaya parkir
lama = int(input("Lama parkir (jam): "))
vip = input("Apakah member VIP? (ya/tidak): ")
if vip == "ya":
    biaya = 0
else:
    hari = lama // 24
    sisa_jam = lama % 24
    biaya = hari * 20000
    if sisa_jam <= 2:
        tambahan = 5000
    else:
        tambahan = 5000 + (sisa_jam - 2) * 3000
        if tambahan > 20000:
            tambahan = 20000
        biaya += tambahan
