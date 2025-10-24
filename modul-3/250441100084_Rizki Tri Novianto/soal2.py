sandi = "25084"
error = 0  


while error < 3:
    pin = input("masukkan PIN: ")  
    
    panjang = 0
    for karakter in pin:
        panjang += 1
    
    if panjang != 5:
        print("PIN harus 5 digit! Coba lagi.")
    
    sandi_benar = True
    for percobaan in pin:
        if percobaan <'0' or percobaan >= '9':
            sandi_benar = False
    
    if not sandi_benar:
        print("PIN harus angka! Coba lagi.")
        break

    elif pin == sandi:
        print("PIN benar, akses diterima")
        akses_diterima = True  
        break

    else:
        error += 1
        kesempatan = 3 - error
        if kesempatan > 0:
            print(f"PIN salah, coba lagi kesempatan anda masih {kesempatan} ")
        
else:
    print("Akses ditolak, kartu diblokir")