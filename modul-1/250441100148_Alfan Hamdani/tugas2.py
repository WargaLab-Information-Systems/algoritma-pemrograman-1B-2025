# Menghitung volume dan luas sebuah balok
# panjang = 10cm
# lebar = 6cm
# tinggi = 4cm

panjang = int(input("Masukkan panjang balok (cm): "))
lebar = int(input("Masukkan lebar balok (cm): "))
tinggi = int(input("Masukkan tinggi balok (cm): "))

volume = panjang * lebar * tinggi
print("Volumenya adalah:", volume, "cm")

luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
print("Luas permukaannya adalah:", luas_permukaan, "cm")