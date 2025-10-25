harga_tiket = 50000

usia = int(input("Masukkan usia anda: "))
status_pelajar = str(input("Apakah anda pelajar sma? (ya/tidak): ")).lower()
hari = str(input("Masukkan Hari: "))
diskon = 0  
if usia < 12:
    if 50 > diskon:
        diskon = 50

if status_pelajar == "ya":
    if 30 > diskon:
        diskon = 30

if hari == "selasa":
    if 20 > diskon:
        diskon = 20

harga_diskon = harga_tiket - (harga_tiket * diskon / 100)

print("Harga tiket yang harus dibayar: Rp",int(harga_diskon),"(Diskon yang kamu dapat adalah", diskon, "%)")

