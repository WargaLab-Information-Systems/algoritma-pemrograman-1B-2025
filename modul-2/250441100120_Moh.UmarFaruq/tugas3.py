print("Welcome to the Mall!")

lama_parkir = int(input("Masukkan lama parkir (jam): "))
status_vip = input("Apakah Anda member VIP? (ya/tidak): ")

if status_vip.lower() == "ya":
    biaya_parkir = 0
else:
    if lama_parkir <= 2:
        biaya_parkir = 5000
    else:
        biaya_parkir = 5000 + (lama_parkir - 2) * 3000
        if biaya_parkir > 20000:
            biaya_parkir = 20000

print(f"Biaya parkir yang harus dibayar adalah Rp{biaya_parkir}")
