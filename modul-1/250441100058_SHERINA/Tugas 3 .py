import math

bola_merah = 8
bola_biru = 6
total_bola = bola_merah +bola_biru
bola_diambil = 3

kombinasi_total = math.comb(total_bola, bola_diambil)

print(f"Jumlah kemungkinan kombinasi 3 bola yang dapat diambil adalah: {kombinasi_total}")
