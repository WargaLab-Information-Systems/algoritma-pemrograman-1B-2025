PIN_saya = 25054
kesempatan = 3

for i in range(kesempatan):
    pin = int(input("Masukkan PIN 5 digit: "))
    if pin == PIN_saya:
        print("PIN benar, akses diterima.")
        break
    else:
        print("PIN salah, coba lagi.")

else:
    print("Akses ditolak, kartu diblokir.")
