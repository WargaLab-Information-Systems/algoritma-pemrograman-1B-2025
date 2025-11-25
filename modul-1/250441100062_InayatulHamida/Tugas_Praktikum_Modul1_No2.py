2. # Ukuran balok
panjang_balok = 10  # cm
lebar_balok = 6     # cm
tinggi_balok = 4    # cm

panjang = int(input("masukkan panjang balok(cm): "))
lebar = int(input("masukkan lebar balok(cm): "))
tinggi = int(input("masukkan tinggi balok(cm): "))

# Menghitung volume
volume = panjang_balok * lebar_balok * tinggi_balok

# Menghitung luas permukaan
luas_permukaan = 2 * (panjang_balok * lebar_balok + panjang_balok * tinggi_balok + panjang_balok * tinggi_balok)

# Menampilkan hasil
print(f"Volume balok: {volume} cm³")
print(f"Luas permukaan balok: {luas_permukaan} cm²")