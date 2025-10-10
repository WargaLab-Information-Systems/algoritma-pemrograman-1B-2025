# PROGRAM BIAYA PARKIR DENGAN MAKSIMAL PER HARI
# Menggunakan konsep: Modul 1 (Variabel, Operator Aritmatika) & Modul 2 (If-Elif-Else)

# MODUL 1: VARIABEL & INPUT
# Menerima input lama parkir (jam) dan status VIP

try:
    lama_parkir = int(input("Masukkan lama parkir (jam): "))
except ValueError:
    print("[ERROR] Input lama parkir harus berupa angka bulat.")
    lama_parkir = 0 # Default jika input salah
    
status_vip = input("Apakah pengunjung adalah member VIP? (ya/tidak): ").lower()

# MODUL 1: VARIABEL untuk Konstanta Tarif
TARIF_2_JAM_PERTAMA = 5000
TARIF_PER_JAM_BERIKUTNYA = 3000
MAKSIMAL_TARIF_PER_HARI = 20000
JUMLAH_JAM_SEHARI = 24

total_biaya = 0

# MODUL 2: PENYELEKSIAN KONDISI UTAMA (If-Else)
# 1. Cek Status VIP (Prioritas Utama)
if status_vip == "ya":
    total_biaya = 0
    print("\n[INFO] Pengunjung adalah member VIP. Biaya parkir: Rp0.")
    
# 2. Jika Bukan VIP, Lakukan Perhitungan Normal
else:
    print("[INFO] Menghitung tarif parkir normal...")
    
    # MODUL 1: OPERATOR ARITMATIKA (Pembagian Bulat // dan Sisa Bagi %)
    # Memecah total jam parkir menjadi Hari Penuh dan Sisa Jam
    jumlah_hari_penuh = lama_parkir // JUMLAH_JAM_SEHARI
    sisa_jam = lama_parkir % JUMLAH_JAM_SEHARI
    
    # Menghitung Biaya Hari Penuh (Setiap hari penuh dikenakan batas maksimal)
    biaya_penuh = jumlah_hari_penuh * MAKSIMAL_TARIF_PER_HARI
    
    # Menghitung Biaya Sisa Jam
    biaya_sisa_sementara = 0
    
    # MODUL 2: PENYELEKSIAN KONDISI untuk Sisa Jam (If-Elif-Else)
    if sisa_jam == 0:
        biaya_sisa_sementara = 0
    elif sisa_jam <= 2:
        # Tarif 2 jam pertama
        biaya_sisa_sementara = TARIF_2_JAM_PERTAMA
    else:
        # Tarif jam berikutnya (MODUL 1: OPERATOR ARITMATIKA)
        biaya_jam_berikutnya = (sisa_jam - 2) * TARIF_PER_JAM_BERIKUTNYA
        biaya_sisa_sementara = TARIF_2_JAM_PERTAMA + biaya_jam_berikutnya
        
    # MODUL 2: PENYELEKSIAN KONDISI untuk Cek Batas Maksimal Harian Sisa Jam
    # Biaya sisa jam harus tetap dibatasi maksimal Rp20.000
    if biaya_sisa_sementara > MAKSIMAL_TARIF_PER_HARI:
        biaya_sisa = MAKSIMAL_TARIF_PER_HARI
        print("[INFO] Biaya sisa jam mencapai batas maksimal harian.")
    else:
        biaya_sisa = biaya_sisa_sementara

    # MODUL 1: OPERATOR ARITMATIKA (Penjumlahan)
    # Total Biaya Keseluruhan
    total_biaya = biaya_penuh + biaya_sisa

# OUTPUT HASIL
print("\n========== STRUK PARKIR ==========")
print(f"Lama Parkir Total : {lama_parkir} jam")
print(f"Status VIP : {status_vip.upper()}")
print(f"Biaya Hari Penuh ({jumlah_hari_penuh} hari @ Rp{MAKSIMAL_TARIF_PER_HARI:,.0f}) : Rp{biaya_penuh:,.0f}")
print(f"Biaya Sisa Jam ({sisa_jam} jam) : Rp{biaya_sisa:,.0f}")
print("----------------------------------")
print(f"Total Biaya Parkir: Rp{total_biaya:,.0f}") 
print("==================================")