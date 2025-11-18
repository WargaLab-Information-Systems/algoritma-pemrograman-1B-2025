# #Soal Nomor 2
pin_yang_benar = 25104
percobaan = 0

while percobaan <3:
    pin =input("masukkan pin 5 digit:")
    if pin == pin_yang_benar:
        print("pin benar, akses diterima")
        break
    else:
        print("pin salah, coba lagi")
        percobaan = percobaan + 1
if percobaan == 3:
    print("akses ditolak, kartu diblokir")