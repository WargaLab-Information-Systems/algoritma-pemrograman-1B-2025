print("MENGHITUNG VOLUME & LUAS BALOK ")

panjang = 10
lebar = 6
tinggi = 4

panjang = int(input("Masukkan panjang balok (cm): "))
lebar = int(input("Masukkan lebar balok (cm): "))
tinggi = int(input("Masukkan tinggi balok (cm): "))

volume = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print("Panjang balok:", panjang, "cm")
print("Lebar balok:", lebar, "cm")
print("Tinggi balok:", tinggi, "cm")
print("Volume balok:", volume, "cm³")
print("Luas permukaan balok:", luas_permukaan, "cm²")