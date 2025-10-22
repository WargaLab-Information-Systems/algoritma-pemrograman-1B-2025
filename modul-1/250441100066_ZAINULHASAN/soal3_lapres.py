bola_merah = 8
bola_biru = 6
total_bola = bola_merah + bola_biru
total_diambil = 3
faktorial_total = 14*13*12*11*10*9*8*7*6*5*4*3*2*1
faktorial_diambil = 3*2*1
faktorial_sisa = 11*10*9*8*7*6*5*4*3*2*1
jumlah_kombinasi = faktorial_total // (faktorial_diambil * faktorial_sisa)
print("jumlah kemungkinan kombinasi diambil:",total_diambil,"bola dari",total_bola,"bola adalah:",jumlah_kombinasi)