#soal no 3
from math import comb
bola_merah = 8
bola_biru =6
total_bola = bola_merah + bola_biru
total_kombinasi = comb(total_bola, 3)
print(f"Jumlah kemungkinan kombinasi pengambilan 3 bola dari {total_bola} bola adalah: {total_kombinasi}")