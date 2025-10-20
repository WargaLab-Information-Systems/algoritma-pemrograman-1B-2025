# Simulasi mesin ATM sederhana

PIN_BENAR = "080701"  # contoh PIN (X=2, Y=3)
kesempatan = 3

for percobaan in range(kesempatan):
    pin = input("Masukkan PIN (5 digit): ")
    if pin == PIN_BENAR:
        print("PIN benar, akses diterima.")
        break
    else:
        sisa = kesempatan - (percobaan + 1)
        if sisa > 0:
            print(f"PIN salah, coba lagi. Kesempatan tersisa: {sisa}")
        else:
            print("Akses ditolak, kartu diblokir.")