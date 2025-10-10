# Harga tiket normal
harga_normal = 50000
# Variabel untuk menyimpan diskon terbesar
diskon_terbesar = 0

# Input data dari pengguna
usia = int(input("Masukkan usia Anda (tahun): "))
status_pelajar = input("Apakah Anda pelajar SMA dengan kartu pelajar? (ya/tidak): ").lower()
hari = input("Masukkan hari ini (misal: Senin, Selasa, Minggu): ").lower()

# --- PENYELEKSIAN KONDISI UNTUK MENENTUKAN DISKON TERBESAR ---

# 1. Diskon Anak-anak (< 12 tahun)
if usia < 12:
    diskon_anak = 50  # Diskon 50%
else:
    diskon_anak = 0

# 2. Diskon Pelajar SMA (dengan kartu pelajar)
if status_pelajar == "ya":
    diskon_pelajar = 30  # Diskon 30%
else:
    diskon_pelajar = 0

# 3. Diskon Hari Selasa (promo)
if hari == "selasa":
    diskon_selasa = 20  # Diskon 20%
else:
    diskon_selasa = 0

# Menentukan diskon terbesar
# Membandingkan diskon_anak dan diskon_pelajar
if diskon_anak >= diskon_pelajar:
    diskon_terbesar = diskon_anak
else:
    diskon_terbesar = diskon_pelajar

# Membandingkan diskon terbesar sementara dengan diskon_selasa
if diskon_selasa > diskon_terbesar:
    diskon_terbesar = diskon_selasa

# --- PERHITUNGAN HARGA AKHIR ---

# Menghitung persentase diskon dalam bentuk desimal (misal 50% = 0.50)
persentase_diskon = diskon_terbesar / 100  # Menggunakan operator Pembagian (/) [cite: 247]

# Menghitung jumlah diskon (Rp)
jumlah_diskon = harga_normal * persentase_diskon # Menggunakan operator Perkalian (*) [cite: 247]

# Menghitung harga tiket yang harus dibayar
harga_tiket = harga_normal - jumlah_diskon # Menggunakan operator Pengurangan (-) [cite: 247]

# --- OUTPUT HASIL ---
print("\n--- Rincian Tiket ---")
print("Harga Normal Tiket: Rp", harga_normal)
print("Diskon yang Diterapkan: ", diskon_terbesar, "%")
print("Jumlah Diskon (Rp): Rp", int(jumlah_diskon)) # int() agar tidak ada koma pada uang
print("Harga Tiket yang Harus Dibayar: Rp", int(harga_tiket))
print("---------------------")
