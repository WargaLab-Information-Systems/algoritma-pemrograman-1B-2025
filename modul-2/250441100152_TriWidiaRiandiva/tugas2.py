# Program Menghitung Harga Tiket Bioskop

harga_tiket = 50000
usia = int(input("Masukkan usia: "))
status_pelajar = input("Apakah pelajar SMA? (ya/tidak): ").lower()
hari = input("Masukkan hari: ")

# Menentukan diskon 
diskon = 0
if usia <= 12:
    diskon = 0.50
elif status_pelajar == "ya":
    diskon = 0.30
elif hari == "selasa":
    diskon = 0.20

# Menghitung harga setelah diskon
harga_setelah_diskon = harga_tiket - (harga_tiket * diskon)

print("Harga tiket yang harus dibayar: Rp", int(harga_setelah_diskon))
