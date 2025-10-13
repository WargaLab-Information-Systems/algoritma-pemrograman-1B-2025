# nilai = 80 
# if nilai >= 70 :
#     print("B")
# print("\n")

# umur = 17 
# if umur >= 17 :
#     print("boleh buat sim")
# else :
#     print("belum boleh buat sim")
# print("\n")

# nilai = int(input("Masukan nilai kamu: "))
# if nilai >= 85 :
#     print("A")
# elif nilai >= 80 :
#     print("B")
# elif nilai >= 70 :
#     print("C")
# else :
#     print ("D")
# print("\n")

# uang = int(input("Berapa Uang Kamu: "))
# hari = str(input("Sekarang Hari Apa: "))
# if uang >= 30000:
#     if hari == "Minggu":
#         print("Beli buku di hari diskon")
#     else:
#         print("Beli buku harga normal")
# print("\n")


kendaraan = input("Masukan jenis kendaraan anda :")

if kendaraan == "mobil" :
    tarif = 15000
elif kendaraan == "truk_kecil" :
    tarif = 25000
elif kendaraan == "truk_besar" :
    tarif = 40000
else :
    print("kendaraan anda tidak termasuk")
    exit()


metode = input("Masukan metode pembayaran (e-money/tunai): ")

if metode == "e-money" :
   jam = int(input("Masukan jam pembayaran(0-23):"))
   if 23 <= jam or jam <5 :
       diskon = 0.20
   else :
       diskon = 0.10
else :
    diskon = 0.0
                   

total = tarif - (tarif * diskon)

print("\n")
print(f"Tarif dasar             : Rp{tarif}")
print(f"Diskon                  : {diskon * 100}%")
print(f"Total yang harus dibayar: Rp{int(total)}")


a1sa = int(input("Masukan umur a1sa :"))

if a1sa <= 0 or a1sa <= 17 :
    print("a1sa masih belum cukup umur")
elif a1sa == 18 :
    print("alsa sudah cukup umur")
else : 
    print("alsaa ngangur jirr")