#total bola&yang diambil
banyak_bola_merah = 8
banyak_bola_biru = 6
diambil = 3

total_bola_dikotak= banyak_bola_merah + banyak_bola_biru
bola_yang_diambil = diambil

import math
kombinasi_bola = math.comb(total_bola_dikotak, bola_yang_diambil)
print("kemungkinan jumlah kombinasi bola yang dapat diambil yaitu:", kombinasi_bola )