def hitung_biaya_parkir(jam_parkir: int, vip: str) -> int:
    if vip.strip().lower() == "ya":
        return 0
    
    tarif_awal = 5000
    tarif_per_jam = 3000
    tarif_maksimum = 20000

    if jam_parkir <= 2:
        biaya = tarif_awal
    else:
        biaya = tarif_awal + (jam_parkir - 2) * tarif_per_jam

    return min(biaya, tarif_maksimum)

# Program utama
print("=== Sistem Tarif Parkir Mall ===")
jam_parkir = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah Anda member VIP? (ya/tidak): ")

biaya = hitung_biaya_parkir(jam_parkir, vip)
print(f"Total biaya parkir: Rp {biaya:,}")