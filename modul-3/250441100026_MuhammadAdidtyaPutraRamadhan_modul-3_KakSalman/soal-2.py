print("Simulasi Mesin ATM")
pin_benar = "25026"
kesempatan = 3
gagal = 0

while gagal < kesempatan:
    pin = input("Masukkan PIN 5 digit: ")
    if pin == pin_benar:
        print("PIN benar, akses diterima")
        break
    else:
        gagal += 1
        if gagal == kesempatan:
            print("Akses ditolak, kartu diblokir")
        else:
            print("PIN salah, coba lagi")