bola_merah = 8
bola_biru = 6
total_bola = bola_merah + bola_biru
print("total bola merah dan biru:", total_bola)
bola_yang_diambil = 3
kombinasi = (total_bola * (total_bola - 1) * (total_bola - 2)) / (bola_yang_diambil * (bola_yang_diambil - 1) * (bola_yang_diambil - 2))
print("Kemungkinan kombinasi bola yang dapat diambil:", kombinasi) 