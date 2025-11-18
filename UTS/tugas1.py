harga_motor_matic = 50000
harga_motor_trail = 100000
harga_motor_sport = 75000

diskon = 0
sewa = 0
total = 0
asuransi = 15000
kupon = 0

sewa = int(input("sewa motor berapa hari : "))
motor = input("motor yang mau di sewa : ")
harga = int(input("berapa harga sewa motor : "))
kupon = input("masukan kupon : ")
total = 0

if sewa <3 :
        print(harga)
if sewa >3:
    print(harga + 15000)
if total >150000:
    diskon = 10
    print(total)
