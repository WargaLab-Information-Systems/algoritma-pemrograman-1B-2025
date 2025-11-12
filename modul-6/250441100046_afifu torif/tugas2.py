t1 = (3, 1, 4)
t2 = (1, 5, 9)

# 1. Gabungkan kedua tuple
gabungan = t1 + t2

# 2. Hapus duplikat tetapi tetap mempertahankan urutan awal
hasil_tanpa_duplikat = []
for angka in gabungan:
    if angka not in hasil_tanpa_duplikat:
        hasil_tanpa_duplikat.append(angka)

# 3. Urutkan secara menurun (descending)
hasil_urut = sorted(hasil_tanpa_duplikat, reverse=True)

# 4. Ubah kembali ke bentuk tuple
hasil_akhir = tuple(hasil_urut)

print("Hasil akhir:", hasil_akhir)