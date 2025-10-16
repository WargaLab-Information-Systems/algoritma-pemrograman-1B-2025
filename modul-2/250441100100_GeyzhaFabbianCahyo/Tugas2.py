# Soal 2 tiket biskop

harga_normal = 50000
umur_anak = int(input("Masukan umur anda                  : "))
pelajar_sma = input("Apakan kamu pelajar sma dengan kartu pelajar (ya/tiidak): ")
hari = input("Sekarang hari apa                  : ")


if umur_anak <= 12 :
    diskon =  0.50 
elif pelajar_sma == "ya"  :
    diskon = 0.30
elif hari == "selasa"  :
    diskon = 0.20
else :
    diskon = 0

diskon_didapat = diskon * 100
harga_bayar = harga_normal * (1 - diskon)

print(f"Diskon yang didapat : {diskon_didapat}%")
print(f"Harga yang harus dibayar: Rp {int(harga_bayar)}")