#menghitung volume dan luas permukaan balok

panjang = int(input("panjang balok: "))
lebar = int(input("lebar balok: "))
tinggi = int(input("tinggi balok: "))

#volume dan luas permukaan
volume = panjang * lebar * tinggi
print("volume balok yaitu =", volume)

luas_permukaan = 2 * (panjang*lebar + panjang*tinggi + tinggi*lebar)
print("luas permukaan balok yaitu =", luas_permukaan)