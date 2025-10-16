# Program untuk menghitung volume dan luas permukaan balok
# Input: panjang, lebar, tinggi dalam cm
panjang = int(input("Diketahui panjang : "))
lebar = int(input("Diketahui lebar :"))
tinggi = int(input("Diketahui tinggi :"))

# Rumus volume balok
volume = panjang * lebar * tinggi
print("Volume balok: ",volume,"cm³")

# Rumus luas permukaan balok
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
print(f"Luas permukaan balok: ",luas_permukaan,"cm²")
