# pin yang benar dan kesempatan memasukkan pin
pin_benar = "25128"  # 2 angka awal dan 3 angka terakhir nim
kesempatan = 3
angka = "0123456789"

for i in range(kesempatan):
    pin = input("masukkan pin (5 digit): ") 
    if pin == pin_benar:
        print("pin benar, akses diterima")
        break
    else:
        sisa_kesempatan = kesempatan - (i + 1)
        if sisa_kesempatan > 0:
            print("pin salah, coba lagi. sisa percobaan:", sisa_kesempatan )
        else:
            print("akses ditolak, kartu diblokir")
