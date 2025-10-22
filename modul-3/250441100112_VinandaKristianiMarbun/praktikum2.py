PIN_BENAR = "25112"  

kesempatan = 3

while kesempatan > 0:
    pin = input("Masukkan PIN (5 digit): ")

    if pin == PIN_BENAR:
        print("PIN benar, akses diterima.")
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print("PIN salah, coba lagi.")
        else:
            print("Akses ditolak, kartu diblokir.")