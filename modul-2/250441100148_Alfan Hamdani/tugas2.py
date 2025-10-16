# Harga tiket sebuah bioskop
usia = int(input("Masukkan usia Anda (dalam tahun): "))
status_pelajar = input("Apakah Anda pelajar SMA dan memiliki kartu pelajar? (ya/tidak): ")
hari = input("Masukkan hari kunjungan (contoh: Senin, Selasa, dst.): ")

# Harga dasar
harga_normal = 50000
diskon = 0

# cek kondisi diskon
if usia < 12:
    diskon = 50
elif status_pelajar == "ya":
    diskon = max(diskon, 30)
elif hari == "selasa":
    diskon = max(diskon, 20)

# Hitung harga akhir
harga_diskon = harga_normal - (harga_normal * diskon // 100)

print("Harga tiket yang harus dibayar: Rp.", harga_diskon)