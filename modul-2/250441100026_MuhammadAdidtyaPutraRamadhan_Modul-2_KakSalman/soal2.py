harga_normal = 50000

usia = int(input("Masukkan usia: "))
pelajar = input("Apakah Anda pelajar SMA dengan kartu pelajar? (ya/tidak):")
hari = input("Masukkan hari (Senin, Selasa, Rabu, dst): ")

diskon = 0

if usia <  12:
    diskon = 50
if pelajar == "ya" and diskon < 30:
    diskon = 30
if hari == "Selasa" and diskon < 20:
    diskon = 20

harga_diskon = harga_normal - (harga_normal * diskon / 100)

print(f"Hari: {hari}")
print(f"Usia: {usia} tahun")
print(f"Status pelajar: {pelajar}")
print(f"Diskon yang digunakan: {diskon}%")
print(f"Harga  yang harus dibayar: Rp {int(harga_diskon)}")