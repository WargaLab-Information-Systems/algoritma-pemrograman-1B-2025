#tarif parkir mall
lama_parkir = int(input("berapa lama kamu parkir (jam): "))
status_vip = input("apa kamu member vip? (yes or no): ")

if status_vip == "yes":  #gratis
    biaya_parkir = 0
elif status_vip == "no":   #tidak gratis
    hari = lama_parkir // 24
    sisa_jam = lama_parkir % 24
    biaya_parkir = hari * 20000
    if sisa_jam == 0:
        biaya_parkir += 0
    elif lama_parkir <= 2:
        biaya_parkir += 5000
    else:
        biaya_parkir += 5000 + (sisa_jam - 2) * 3000
        if biaya_parkir - (hari * 20000) > 20000:
           biaya_parkir = (hari * 20000) + 20000
        
else:
    print("input salah,coba ketik yes or no")
    biaya_parkir = 0


print("total biaya parkir yang harus kamu bayar: rp", biaya_parkir)