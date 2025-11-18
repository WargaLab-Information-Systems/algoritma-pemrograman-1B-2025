pin_saya = "25038"
kesempatan = 3

for i in range(kesempatan):
    pin = input("masukkan pin (5 digit) : ")
    if pin == pin_saya:
        print("PIN benar, akses diterima")
        break
    else:
        print("PIN salah, coba lagi")
else:
    print("akses ditoloak, kartu diblokir")