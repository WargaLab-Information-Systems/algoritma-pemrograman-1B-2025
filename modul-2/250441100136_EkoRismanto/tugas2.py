# Program Harga Tiket Bioskop dan Diskon
HTM = 50000

usia = int(input("Masukkan Usia Anda: "))
status_pelajar = input("Apakah Anda pelajar SMA dengan kartu pelajar? (ya/tidak): ")
hari = input("Hari apa sekarang? ")
diskon = 0

if usia < 12:
    diskon = 50
if status_pelajar == "ya":
    diskon = 30
if hari == "selasa":
    diskon = 20
else :
    print("ini adalah HTM anda")

bayar = HTM - (HTM * diskon  // 100)
print("Harga tiket yang harus dibayar: Rp", bayar)