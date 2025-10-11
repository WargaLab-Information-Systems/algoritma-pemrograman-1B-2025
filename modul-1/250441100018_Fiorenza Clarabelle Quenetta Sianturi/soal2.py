print("volume dan luas permukaan balok")

panjang = int(input("masukkan panjang (cm): "))
lebar = int(input("masukkan lebar (cm) : "))
tinggi = int(input("masukkan tinggi (cm) : "))

volume = panjang * lebar * tinggi
luas_permukaan = 2* (panjang*lebar) + (panjang*tinggi) + (lebar*tinggi)

print("========hasil========")
print("volume balok adalah ", volume)
print("luas permukaan balok adalah ", luas_permukaan)