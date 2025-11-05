total_kesalahan = 0
batas_kesalahan = 3
pin_saya = 25080

while total_kesalahan < batas_kesalahan:
    pin_atm = int(input("Silahkan masukkan PIN ATM anda : "))
    if pin_atm == pin_saya:
        print("“PIN benar, akses diterima”")
        break
else:
    total_kesalahan += 1
    percobaan_input = batas_kesalahan - total_kesalahan
    print("Sisa percobaan mu",percobaan_input )
if total_kesalahan == batas_kesalahan:
    print("“Akses ditolak, kartu diblokir”")