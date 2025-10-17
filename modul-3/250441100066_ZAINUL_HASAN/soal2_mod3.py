PIN_SAYA = 25066
kesempatan = 3

for i in range(kesempatan):
    pin = int(input("Masukkan PIN (5 digit): "))
    if pin == PIN_SAYA:
        print("PIN benar, akses diterima")
        break
    else:
        print("PIN salah, coba lagi")
else:
    print("Akses ditolak, kartu diblokir")