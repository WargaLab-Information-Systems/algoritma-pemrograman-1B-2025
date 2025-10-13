lama_parkir = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah Anda member VIP? (ya/tidak): ").lower()

# Cek status VIP
if vip == "ya":
    biaya = 0 
    keterangan = "Anda adalah member VIP, parkir gratis."
    print(keterangan)
else:
    hari = lama_parkir // 24
    sisa = lama_parkir % 24
    biaya_harian = hari * 20000

    if sisa == 0:
        biaya_sisa = 0
        rincian_sisa = ""
    elif sisa <= 2:
        biaya_sisa = 3000
        rincian_sisa = f"{sisa} jam = Rp{biaya_sisa}"
    else:
        biaya_sisa = 5000 + (sisa - 2) * 3000
        rincian_sisa = f"{sisa} jam = Rp{biaya_sisa} (Rp5000 untuk 2 jam pertama + Rp3000 x {sisa - 2} jam)"

    total_biaya = biaya_harian + biaya_sisa

    # Cetak rincian
    print("\n=== Rincian Biaya Parkir ===")
    if hari > 0:
        print(f"{hari * 24} jam = Rp{biaya_harian}")
    if sisa > 0:
        print(rincian_sisa)
    print(f"Total biaya parkir: Rp{total_biaya}")
