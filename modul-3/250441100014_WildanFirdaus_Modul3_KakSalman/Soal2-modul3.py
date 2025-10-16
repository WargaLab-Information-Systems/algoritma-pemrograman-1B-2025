pin_saya = "25014"
kesempatan = 5

for i in range(kesempatan):
    pin = input("masukkan pin (5 digit) : ")
    if pin == pin_saya:
        print("PIN benar, akses diterima")
        break
    else:
        print("PIN salah, coba lagi")
else:
    print("akses ditolak, kartu diblokir")