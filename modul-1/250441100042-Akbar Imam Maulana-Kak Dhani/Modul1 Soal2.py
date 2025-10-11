print(" Menghitung Volume dan Luas Permukaan Balok")

 #ukuran balok
panjang = 10
lebar = 6    
tinggi = 4   

 #hitung volume
volume = (panjang * lebar * tinggi)
print(f"Volume balok: {volume} cm^3")

 #hitung luas permukaan
luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi)) 
print(f"Luas permukaan balok: {luas_permukaan} cm^2")