motor_matic = 50000
motor_trail = 100000
motor_sport = 75000
asuransi = 15000  
sewa = 3          
diskon = 0.10              
diskon_tambahan = 0.5
kupon = "AconkGG"


harga_sewa = 0
diskon = 0

while True :
    if sewa >= 3 :
        print("total harga sewa:, ")
        break
    elif motor_matic :
        print("Total harga rental motor:, motor_matic")
    elif motor_trail :
        print("Total harga rental motor:, motor_trail")
    elif motor_sport :
        print("Total harga sewa motor:, motor_sport")
        if diskon in harga_sewa :
            if harga_sewa > 150000 :
                diskonn = 0.10
            if diskon_tambahan :
                diskon_tambahan = input("Masukkan kupon")

