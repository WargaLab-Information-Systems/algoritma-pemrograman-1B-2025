# Program simulasi sederhana mesin ATM
pin_benar = "25148"

kesempatan = 3 # 3 kali kesempatan

for i in range(kesempatan):
    pin = input("Masukkan PIN (5 digit): ")

    # cek apakah PIN berupa angka dan 5 digit
    if not pin.isdigit() or len(pin) != 5:
        print("PIN harus berupa 5 digit angka!")
        continue

    # cek apakah pin benar
    if pin == pin_benar:
        print("PIN benar, akses diterima")
        break
    else:
        print("PIN salah, coba lagi")

else:
    print("Akses ditolak, kartu diblokir")