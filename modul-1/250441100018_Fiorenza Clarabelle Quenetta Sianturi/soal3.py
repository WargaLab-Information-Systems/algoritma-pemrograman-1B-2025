bm = 8
bb = 6
bola_diambil = 3

total_bola = bm+bb

#menghitung kombinasi
pembilang = total_bola * (total_bola-1) * (total_bola-2)
penyebut = bola_diambil * (bola_diambil-1) * (bola_diambil-2)
kombinasi = pembilang//penyebut

print("Total kombinasi bola yang diambil adalah: ", kombinasi)