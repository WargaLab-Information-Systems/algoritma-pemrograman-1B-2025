print(" RENTAL MOTOR ACONK ")
sewa = 0
pilih_motor = int(input("Kamu mau sewa apa 1.sewa matic 2. sewa trail 3. sewa sport 1/2/3 ?"))
if pilih_motor == "1":
    sewa= 5000000
elif pilih_motor == "2":
    sewa= 10000000
elif pilih_motor == "3":
    sewa= 7500000
sewamu = sewa
biaya_asuransi = 1500000
lama_sewa = int(input("Masukkan lama penyewaan"))

if lama_sewa <= 3:
    print("kamu sewa lebih 3 hari ")
    asuransi = biaya_asuransi
    print(asuransi)

    sewa0 = sewamu + asuransi
    print(sewa0)

    diskon10 = 0.1

diskon_tambahan = 0.5
diskonmula = 0
diskon = input("masukkkan kupon = ")
if diskon == "AconkGG":
    diskon_akhir = diskonmula + diskon_tambahan
    

total_sewa = sewa0 * diskon_akhir
print(total_sewa)