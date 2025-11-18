3 # Input dari pengguna
lama_parkir = int(input("Masukkan lama parkir (dalam jam): "))
status_vip = input("Apakah Anda member VIP? (ya/tidak): ")

# Inisialisasi biaya
biaya = 0

if status_vip == 'ya':
    biaya = 0  # Biaya parkir gratis untuk member VIP
else:
    # Biaya untuk 2 jam pertama
    biaya = 5000
    
    # Jika lama parkir lebih dari 2 jam, hitung biaya tambahan
    if lama_parkir > 2:
        jam_tambahan = lama_parkir - 2
        biaya = biaya + jam_tambahan * 3000
    
    # Batasi biaya maksimal per hari
    if biaya > 20000:
        biaya = 20000

# Tampilkan hasil
print(f"Total biaya parkir: Rp{biaya}")