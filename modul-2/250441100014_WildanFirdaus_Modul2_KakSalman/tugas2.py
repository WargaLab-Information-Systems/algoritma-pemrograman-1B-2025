harga_normal = 50000

usia = int(input("masukkan usia kita: "))
status_pelajar = input("apakah anda pelajar SMK dengan kartu pelajar? (ya/tidak): ")
hari = input("sekarang hari apa? ")
diskon = 0

if usia < 12:   
   diskon = 50
elif status_pelajar == "ya":
   diskon = 30
elif hari == "rabu":
   diskon = 20
else :
   print("harga_normal")

bayar = harga_normal - (harga_normal * diskon // 100)
print("harga tiket yang harus di bayar: Rp", bayar)