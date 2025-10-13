tiket = 50000

hari = (input("Masukkan hari: "))
usia = int(input("Masukkan usia: "))
status_pelajar = input("Apakah SMA? (ya/tidak): ")

if usia <= 12:
    D = 0.5
    diskon = tiket * D
    total1 = tiket - diskon
    print("Total harga tiket dengan diskon usia:", total1)
elif status_pelajar == "ya":
    D = 0.3
    diskon = tiket * D
    total2 = tiket - diskon
    print("Total harga tiket dengan diskon pelajar:", total2)
elif hari == "selasa":
    D = 0.2
    diskon = tiket * D
    total3 = tiket - diskon
    print("Total harga tiket dengan diskon hari selasa:", total3)
else:
    print("Total harga tiket tanpa diskon:", tiket)