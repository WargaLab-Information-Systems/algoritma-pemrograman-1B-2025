# PIN yang benar
pin_benar = int(input("Masukkan PIN awal (XXYYY): "))

# Pastikan PIN adalah 5 digit
while len(str(pin_benar)) != 5:
    pin_benar = int(input("PIN harus 5 digit, coba lagi: "))

kesempatan = 3

while kesempatan > 0:
    # Minta user memasukkan PIN
    pin_user = int(input("Masukkan PIN Anda: "))
    
    # Pastikan PIN adalah 5 digit
    while len(str(pin_user)) != 5:
        pin_user = int(input("PIN harus 5 digit, coba lagi: "))

    # Periksa apakah PIN benar
    if pin_user == pin_benar:
        print("PIN benar, akses diterima")
        break
    else:
        kesempatan -= 1
        print("PIN salah, coba lagi. Kesempatan tersisa: ",kesempatan)

if kesempatan == 0:
    print("Akses ditolak, kartu diblokir")
    