panjang = int(input("Masukkan panjang balok (10cm) = "))
lebar = int(input("Masukkan lebar balok (6cm) = "))
tinggi = int(input("Masukkan tinggi balok (4cm) = "))

volume = panjang * lebar * tinggi
luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print("Volume balok adalah = ", volume, "cm^3")
print("Luas balok adalah = ", luas, "cm^2")