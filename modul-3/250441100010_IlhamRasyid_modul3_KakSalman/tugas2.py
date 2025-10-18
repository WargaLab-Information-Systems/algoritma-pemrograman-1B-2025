pinku = "25010"
pinsaya = input("masukkan pin baru :")
kesempatan = 3

for i in range(kesempatan):
    pin = input("masukkan pin (5 digit) : ")
    if pin == pinsaya:
        print("PIN benar, akses diterima")
        break
    else:
        print("PIN salah, coba lagi")
else:
    print("akses ditoloak, kartu diblokir")