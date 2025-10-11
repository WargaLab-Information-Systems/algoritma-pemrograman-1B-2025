# Program menghitung berapa banyak kemungkinan kombinasi bola yang dapat diambil

# Total bola dalam kotak
bola_merah = 8
bola_biru = 6
bola_diambil = 3
total_bola_dalam_kotak = bola_merah + bola_biru

print("Total bola dalam kotak:", total_bola_dalam_kotak)
 
# hitung kombinasi
faktorial_total_dalam_kotak = 14 * 13 * 12
faktorial_total_bola_diambil = 3 * 2 * 1
kombinasi_bola_yang_dapat_diambil = faktorial_total_dalam_kotak // faktorial_total_bola_diambil

print("Banyaknya kemungkinan kombinasi adalah:", kombinasi_bola_yang_dapat_diambil)