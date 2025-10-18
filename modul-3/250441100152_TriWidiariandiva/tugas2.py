pin_benar = "25152"
kesempatan = 3

while kesempatan > 0:
    pin = input("Masukkan PIN (5 digit): ")
    if pin == pin_benar:
        print("PIN benar, akses diterima")
        break
    else:
        kesempatan -= 1
        print("PIN salah, coba lagi")
else:
    print("Akses ditolak, kartu diblokir")  
