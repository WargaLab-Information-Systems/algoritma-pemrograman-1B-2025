# Program sederhana perulangan
total_harga = 0
jumlah_obat = 0

while True:
    harga = int(input("Masukkan harga obat (pilih 0 jika selesai): "))
    if harga == 0:
        break
    total_harga += harga
    jumlah_obat += 1

if jumlah_obat > 0:
    rata_rata = total_harga // jumlah_obat
else:
    rata_rata = 0

print("Hasil Perhitungan ")
print("Total harga seluruh obat: Rp", total_harga)
print("Jumlah obat yang dibeli :", jumlah_obat)
print("Rata-rata harga obat yang dibeli: Rp", rata_rata)