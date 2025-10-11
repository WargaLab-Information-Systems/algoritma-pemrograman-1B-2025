panjang = int(input("Masukkan panjang dari balok: "))
lebar = int(input("Masukkan lebar dari balok : "))
tinggi = int(input("Masukkan tinggi dari balok : "))

volume = panjang * lebar * tinggi
luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
print("Jadi volume dari balok tersebut adalah : " , volume, )
print("Jadi luas dari balok tersebut adalah : " , luas, )