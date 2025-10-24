motor_matic = 50000
motor_trial = 100000
motor_sport = 75000
asuransi = 0
diskon = 0
subtotal = 0
kupon = " "
hari = True
mulai =""
while mulai == "y":    
    while asuransi <3:
     if motor_matic:
        if subtotal < 15000:
            diskon = 10 // 100
            subtotal = subtotal* diskon
            kupon=(input("masukkan kupon :"))  
              
        if kupon == "AconkGG":
                diskon = 5 // 100
                subtotal = subtotal * diskon
                hari = False
    if motor_trial:
        if subtotal < 15000:
            diskon = 10 // 100
            subtotal = subtotal* diskon
            kupon=(input("masukkan kupon :"))  
              
        if kupon == "AconkGG":
                diskon = 5 // 100
                subtotal = subtotal * diskon
                hari = False
        else:
            asuransi=asuransi
    if motor_sport:
        if subtotal < 15000:
            diskon = 10 // 100
            subtotal = subtotal* diskon
            kupon=(input("masukkan kupon :"))  
              
        if kupon == "AconkGG":
                diskon = 5 // 100
                subtotal = subtotal * diskon
                hari = False
        
    
    else:
            asuransi=asuransi
    asuransi+=1

    
mulai=input("masukkan ya jika ingin menyewa kembali:","ya")
print(mulai)