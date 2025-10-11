panjang = int(input("masukkan panjang balok(10cm) :"))
lebar = int(input("masukkan lebar balok(6cm) :"))
tinggi = int(input("masukkan tinggi balok(4cm) :"))

volume = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print("volume balok adalah", volume, "cm")
print("luas permukaan balok adalah", luas_permukaan, "cm")