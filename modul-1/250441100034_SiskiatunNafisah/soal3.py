total_bola = 14   
r = 3 

atas = total_bola * (total_bola - 1) * (total_bola - 2)
bawah = r * (r - 1) * 1

kombinasi = atas // bawah

print("Jumlah kombinasi jika mengambil", r, "bola =", kombinasi)