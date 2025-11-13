 
motor_matic = 50000
motor_trail = 100000
motor_sport = 75000
sewa = motor_matic, motor_trail, motor_sport
harga = 0
asuransi = 150000
diskon = 0
kupon = "AconkGG"
subtotal = 0
hari = 0

while harga:
    if sewa >= hari :
        print("biaya asuransi:", asuransi)
    elif subtotal >= 150000:
        diskon = diskon == 0.1 
    elif kupon:
        if kupon == "AconkGG":
            diskon == 0.5
    else:
        print("tidak valid")
print = int(input("masukkan nama motor:"))
print = input("masukkan hari:")
print = input("masukkan subtotal:")
print("harga sewa motor:")