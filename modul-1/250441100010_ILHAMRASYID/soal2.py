# menghitung volume dan luas sebuah balok
# panjang = 10cm
# lebar = 6cm
# tinggi = 4cm

panjang = int(input("panjang balok : "))
lebar = int(input("lebar balok : "))
tinggi = int(input("tinggi balok : "))

volume_balok = panjang * lebar * tinggi
luas_balok = 2 * (panjang * lebar) + (panjang * tinggi) + (lebar * tinggi)

print("jadi volume dari balok tersebut adalah = ", volume_balok, "cm^2")
print("jadi luas dari balok tersebut adalah = ", luas_balok, "cm^2")