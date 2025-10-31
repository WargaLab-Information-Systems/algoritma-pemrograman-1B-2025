# Inisialisasi variabel akumulator untuk menyimpan total mingguan
total_gaji = 0
total_lembur = 0
total_bonus_shift_malam = 0

GAJI_POKOK_HARIAN = 100_000
BONUS_SHIFT_MALAM = 50_000

# Perulangan selama 7 hari (seminggu)
for hari in range(1, 8):
    print(f"\nHari ke-{hari}:")
    
    # Input jam lembur dengan validasi
    while True:
        jam_lembur_str = input("Masukkan jumlah jam lembur: ")
        if jam_lembur_str.isdigit() and int(jam_lembur_str) >= 0:
            jam_lembur = int(jam_lembur_str)
            break
        print("Input tidak valid. Masukkan angka positif saja.")
        
    # Input shift malam dengan validasi
    while True:
        shift_malam = input("Apakah shift malam? (y/tidak): ").lower()
        if shift_malam in ['y', 'tidak']:
            break
        print("Input tidak valid. Masukkan 'y' untuk ya atau 'tidak' untuk tidak.")

    # --- Perhitungan Sederhana (Logika hitung_tambahan_lembur) ---
    
    tambahan_lembur = 0 # Inisialisasi tambahan_lembur

    # Logika perhitungan lembur
    if jam_lembur > 8:
        tambahan_lembur = 0
        print("Lembur melebihi batas (di atas 8 jam), tidak dihitung.")
    elif jam_lembur == 8:
        tambahan_lembur = 300_000
    elif jam_lembur >= 6:
        tambahan_lembur = 200_000
    elif jam_lembur >= 4:
        tambahan_lembur = 100_000
    elif jam_lembur >= 1:
        tambahan_lembur = jam_lembur * 25_000
    else: # jam_lembur == 0
        tambahan_lembur = 0
        
    if jam_lembur > 8:
        # Pesan peringatan diulang untuk kejelasan di output
        print("Lembur melebihi batas (di atas 8 jam), tidak dihitung.")
    
    bonus_shift = BONUS_SHIFT_MALAM if shift_malam == 'y' else 0
    
    total_harian = GAJI_POKOK_HARIAN + tambahan_lembur + bonus_shift
    
    # --- Akumulasi nilai harian langsung ke total ---
    total_gaji += total_harian
    total_lembur += jam_lembur
    total_bonus_shift_malam += bonus_shift

    print(f"Gaji hari ke-{hari}: Rp{total_harian:,}")

# --- Rangkuman Akhir (Hanya mencetak variabel total yang sudah dihitung) ---
    
print("\n=== Rangkuman Gaji Mingguan ===")
print(f"Total jam lembur selama seminggu: {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus_shift_malam:,}")
print(f"Total gaji seminggu: Rp{total_gaji:,}")