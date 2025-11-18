#tugas 2
# Input dari pengguna
panjang = float(input("Masukkan panjang balok (cm): "))
lebar = float(input("Masukkan lebar balok (cm): "))
tinggi = float(input("Masukkan tinggi balok (cm): "))

# Hitung volume
volume = panjang * lebar * tinggi

# Hitung luas permukaan
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Tampilkan hasil
print(f"\nVolume balok adalah {volume} cm³")
print(f"Luas permukaan balok adalah {luas_permukaan} cm²")
