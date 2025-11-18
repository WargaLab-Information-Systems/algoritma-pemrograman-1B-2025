print(" Menghitung Berapa Banyak Kemungkinan Kombinasi Bola Yang Dapat Diambil")
 # data bola
bola_merah = 8
bola_biru = 6
 # hitung total bola
total_bola = (bola_merah + bola_biru)
print(f"Total bola: {total_bola} bola")
 # hitung kombinasi pengambilan 3 bola
kombinasi_3_bola = (total_bola * (total_bola - 1) * (total_bola - 2)) / 6
print(f"Kombinasi pengambilan 3 bola: {kombinasi_3_bola} cara")