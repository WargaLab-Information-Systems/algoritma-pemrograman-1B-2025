panjang = int(input("Masukkan panjang balok (cm): "))
lebar = int(input("Masukkan lebar balok (cm): "))
tinggi = int(input("Masukkan tinggi balok (cm): "))
# Menghitung volume balok

volume = panjang * lebar * tinggi 
print(volume)
# Menghitung luas permukaan balok
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar
* tinggi)
print(luas_permukaan)