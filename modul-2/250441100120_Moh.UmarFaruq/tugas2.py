print("Welcome to Cinema")  

usia = int(input("Masukkan usia Anda: "))
status_pelajar = input("Apakah Anda pelajar SMA? (ya/tidak): ")
hari = input("Masukkan hari (Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu): ")

harga_tiket_bioskop = 50000


if usia <= 12:
    diskon = 0.5
elif status_pelajar.lower() == "ya":
    diskon = 0.3
elif hari.capitalize() == "Selasa":
    diskon = 0.2
else:
    diskon = 0

if usia <= 12 and hari.capitalize() == "Selasa":
    diskon = max(0.5, 0.2)
elif usia <= 12 and status_pelajar.lower() == "ya":
    diskon = max(0.5, 0.3)
elif status_pelajar.lower() == "ya" and hari.capitalize() == "Selasa":
    diskon = max(0.3, 0.2)

harga_bayar = harga_tiket_bioskop * (1 - diskon)

print(f"Harga tiket yang harus dibayar adalah Rp{harga_bayar:.2f}")

