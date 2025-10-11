jam = int(input("Berapa jam kamu parkir disini?: "))
vip = input("Apakah kamu anggota VIP disini?: ")

if vip == "ya":
    biaya_parkir = 0
else: 
    if jam <= 2:
        biaya_parkir = 5000
    else:
        biaya_parkir = 5000 + (jam - 2) * 3000

    if biaya_parkir >= 20000:
        biaya_parkir = 20000

print(f"Biaya parkirmu selama {jam} jam adalah Rp.{biaya_parkir}") 