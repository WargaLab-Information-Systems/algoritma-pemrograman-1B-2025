# Program Menghitung Harga Tiket Bioskop

# Harga tiket normal
harga_tiket = 50000
diskon = 0

# Input dari pengguna
usia = int(input("Masukkan usia: "))  

# Cek validitas usia
if usia < 1 or usia > 100:
    print("Usia tidak valid")
    exit()  # Menghentikan program jika usia tidak valid

# Diskon berdasarkan usia
if usia <= 12:
    diskon = 0.5
else:
    pelajar = input("Apakah Anda pelajar SMA yang memiliki kartu pelajar? (ya/tidak): ").lower()
    if pelajar == "ya":
        diskon = 0.3

# Diskon berdasarkan hari
hari = input("Masukkan hari: ").lower()
if hari == "selasa":
    if diskon < 0.2:
        diskon = 0.2

# Hitung harga akhir
harga_akhir = harga_tiket - (harga_tiket * diskon)

# Tampilkan hasil
print("\n=== Hasil Perhitungan Harga Tiket ===")
print(f"Harga tiket normal      : Rp{harga_tiket}")
print(f"Diskon yang diterapkan  : {int(diskon * 100)}%")
print(f"Total yang harus dibayar: Rp{int(harga_akhir)}")
