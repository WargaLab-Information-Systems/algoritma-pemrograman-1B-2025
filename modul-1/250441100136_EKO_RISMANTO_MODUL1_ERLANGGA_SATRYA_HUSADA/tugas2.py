# Menghitung Volume dan Luas Balok
# Panjang = 10#cm
# Lebar = 6cm
# Tinggi = 4cm

Panjang = int(input("Masukan Panjang dari Balok : "))
Lebar = int(input("Masukan Lebar dari Balok : "))
Tinggi = int(input("Masukan tinggi dari Balok : "))

# Menghitung Volume Balok
Volume = Panjang * Lebar * Tinggi
Luas = 2 * ((Panjang * Lebar) + (Panjang * Tinggi) + ( Lebar * Tinggi))

# Hasilnya
print("Volume dari Balok tersebut adalah : ", Volume, "cm^2")
print("Luas dari Balok tersebut adalah : ", Luas, "cm^2")