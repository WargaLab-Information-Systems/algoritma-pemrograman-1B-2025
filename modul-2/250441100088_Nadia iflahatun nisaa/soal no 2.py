#harga tiket bioskop
harga_tiket_normal = 50000

#diskon untuk usia,pelajar,hari
usia = int(input("masukkan usiamu: "))
status_pelajar = input("apakah kamu itu pelajar sma dengan kartu pelajar? (yes or no): ")
hari = input("kamu mau nonton hari apa: ")

#ketentuan diskon
if usia < 12:
    diskon = 50
elif status_pelajar == "yes":
    diskon = 30
elif hari == "selasa":
    diskon = 20
else:
    diskon = 0

#harga after diskon
harga_dibayar = harga_tiket_normal - (harga_tiket_normal * diskon / 100)
print("diskon yang kamu dapatkan:", diskon, "%")
print("total harga tiket yang kamu bayar: rp", harga_dibayar)
