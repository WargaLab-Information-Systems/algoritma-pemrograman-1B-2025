nomer_pin = "25062"
kesempatan = 3

for i in range(kesempatan):
    pin = input("masukkan pin (5 digit) : ")
    if pin == nomer_pin:
        print("PIN benar, akses diterima.")
        break
    else:
        print("PIN salah, coba lagi")
else:
    print("kartu akses ditolak, kartu diblokir.")
    