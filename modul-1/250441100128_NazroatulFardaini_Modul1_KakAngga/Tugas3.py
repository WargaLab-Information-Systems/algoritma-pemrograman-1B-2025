# masukkan bola
bola_merah = 8
bola_biru = 6
bola_diambil = 3
# menghitung total semua bola
total_semua_bola = bola_merah+bola_biru
# menghitung kombinasi bola yang dapat diambil
faktorial_total_semua_bola = 14*13*12*11*10*9*8*7*6*5*4*3*2*1
faktorial_bola_diambil = 3*2*1
faktorial_sisa = 11*10*9*8*7*6*5*4*3*2*1
kombinasi_bola_yang_dapat_diambil = faktorial_total_semua_bola//(faktorial_bola_diambil*faktorial_sisa)
print("rumus kombinasi = n!/(r!x(n-r!))")
print("banyak bola =", kombinasi_bola_yang_dapat_diambil)  