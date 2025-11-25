3. # Total bola
bola_merah = 8
bola_biru = 6
total_bola = 14

# jumlah bola yang diambil
r = 3

# hitungan permutasi (urutan hitung)
permutasi = total_bola * (total_bola - 1) * (total_bola - 2)

# hitung susun 3 bola
susun = r*(r-1)*1

# hasil
kombinasi = permutasi//susun

print("jumlah_bola_yang_diambil",r,"bola =", kombinasi)
