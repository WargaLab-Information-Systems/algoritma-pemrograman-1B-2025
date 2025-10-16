# Nomor 2
harga_tiket = 50000
usia = int(input("Masukan usia:"))
pelajar = input("Apakah anda pelajar SMA dengan kartu pelajar? (ya/tidak):")
hari = input("Masukan hari:")

if usia <= 12:
    diskon = 0.50
elif pelajar == "ya":
    diskon = 0.30
elif hari == "selasa":
    diskon = 0.20
else:
    diskon = 0

diskon_didapat = diskon * 100
harga_bayar = harga_tiket *  diskon

print(f"Diskon yang didapat : {diskon_didapat}%")
print(f"Total harga tiket yang harus dibayar: Rp{int(harga_bayar)}")





#Nomor 3
jam = float(input("Masukkan lama parkir (jam): "))
vip = input("Apakah Anda member VIP? (ya/tidak): ")

# # Jika VIP, gratis
if vip == "ya":
    biaya = 0
else:
    #Hitung jumlah hari penuh dan sisa jam
    hari = jam // 24       #jumlah hari penuh
    sisa_jam = jam % 24     #sisa jam setelah hari penuh

    #Biaya untuk hari penuh
    biaya = hari * 20000        #setiap hari penuh dihitung 20.000

    #Biaya untuk sisa jam (Hari terakhir)
    if sisa_jam == 0 :
        biaya += 0
    elif sisa_jam <= 2:
        biaya += 5000
    else:
        biaya += 5000 + (sisa_jam - 2) * 3000

        #Batas harian tetap 20.000
    if biaya - hari * 20000 > 20000:
        biaya = hari * 20000 + 20000

print(f"Total biaya parkir: Rp {int(biaya)}")



