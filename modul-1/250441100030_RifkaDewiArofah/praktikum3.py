bola_merah = 8
bola_biru = 6
bola_diambil = 3 

total_bola = bola_merah+bola_biru

#menghitung kombinasi
pembilang = total_bola * (total_bola-1) * (total_bola-2)
penyebut = bola_diambil * (bola_diambil-1) * (bola_diambil-2)
kombinasi = pembilang//penyebut

print("Total kombinasi bolaa yang diambil adalah: ", kombinasi)