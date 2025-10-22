#harga sewa
motor_matic = 50000
motor_trail = 100000
motor_sport = 75000

asuransi = 15000
diskon = 0.10
diskon_tambahan = 0.05
lama_sewa = 0
subtotal = 0
kupon_dimasukkan = ""
kupon = "AconkGG"
for i in range(lama_sewa):
    sewa = int(input("masukkan lama sewa: "))
    masukan_kupon = input("masukkan kupon: ")
    if lama_sewa > 3:
        hitung_motor_matic = motor_matic*asuransi
        print("asuransi:", asuransi)
    elif subtotal > 150000:
        print("ada diskon: ", diskon)
    elif kupon_dimasukkan == kupon:
        print("ada diskon tambahan: ",diskon_tambahan)
print(sewa)
print(masukan_kupon)
