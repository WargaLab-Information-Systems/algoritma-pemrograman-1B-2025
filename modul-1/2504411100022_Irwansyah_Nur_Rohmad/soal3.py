
bola_merah = 8 
bola_biru = 6
total_bola = bola_merah + bola_biru
bola_yang_diambil = 3
atas = total_bola * (total_bola - 1) * (total_bola - 2)
bawah = 3 * (3 - 1) * (3 - 2)
hasilnya = atas // bawah
print(" Jadi Banyak kemungkinan kombinasi bola yang dapat diambil adalah : " , hasilnya )