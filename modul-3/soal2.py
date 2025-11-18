PinB = "25030"
salah = 0  

for salah in range (5):
    pin = input("masukkan PIN anda: ")  
    
    acc = True
    for percobaan in pin:
        if percobaan <'0' or percobaan >= '3':
            acc = False
        
    if pin == PinB:
        print("PIN benar, akses diterima")
        akses_diterima = True  
        break

    else:
        salah += 1
        K = 5 - salah
        if K > 0:
            print(f"PIN salah, coba lagi kesempatan anda masih {K} ")
        
else:
    print("Akses ditolak, kartu diblokir")

