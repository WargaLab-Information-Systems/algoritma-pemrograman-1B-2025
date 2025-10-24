
pin_benar = int(input("Masukkan PIN asli (format XXYYY - 2 digit awal dan 3 digit akhir NIM): "))

print("\n=== SIMULASI MESIN ATM ===")
kesempatan = 3

for i in range(kesempatan):
    pin = int(input("Masukkan PIN Anda (5 digit): "))
    if pin == pin_benar:
        print("PIN benar, akses diterima")
        break
    else:
        print("PIN salah, coba lagi")
        if i == kesempatan - 1:
            print("Akses ditolak, kartu diblokir")
