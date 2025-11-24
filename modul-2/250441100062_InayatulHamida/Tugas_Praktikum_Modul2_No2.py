2 # Harga tiket normal
harga_normal = 50000

# Input dari pengguna
usia = int(input("Masukkan usia Anda: "))
# Inisialisasi diskon
diskon = 0

# Cek diskon berdasarkan kondisi
if usia < 1 or usia > 100:
    print("usia tidak valid")
else:
    pelajar = input("Apakah Anda pelajar SMA? (ya/tidak): ")
    hari = input("Hari apa Anda membeli tiket? ")
    if usia < 12 and usia > 0:
        diskon = 0.50  # Diskon 50%
    elif pelajar == 'ya':
        diskon = 0.30  # Diskon 30%
    elif hari == 'selasa': 
        diskon = 0.20  # Diskon 20%

# Hitung harga setelah diskon
harga_setelah_diskon = harga_normal * (1 - diskon)

# Cetak harga tiket yang harus dibayar
print(f"Harga tiket yang harus dibayar: Rp{harga_setelah_diskon:.2f}")

