lama_parkir = int(input("Masukkan lama parkir (jam): "))
status_member = input("Apakah member VIP? (ya/tidak): ")

# Cek status VIP
if status_member == "ya":
    biaya_parkir = 0
    print("Member VIP - Gratis parkir")
else:
    # Hitung bayar parkir
    if lama_parkir <= 2:
        biaya_parkir = 5000
    else:
        
        jam_tambahan = lama_parkir - 2
        biaya_parkir = 5000 + (jam_tambahan * 3000)
    
    # tarif
    if biaya_parkir > 20000:
        biaya_parkir = 20000
print(f"Total lama parkir: {lama_parkir} jam")
print(f"Total biaya parkir: Rp {biaya_parkir:,}")