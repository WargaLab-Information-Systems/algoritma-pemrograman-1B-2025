# Program untuk menghitung jumlah kombinasi memilih 3 bola dari 14 bola (8 merah + 6 biru).
# Kombinasi adalah cara memilih sejumlah item tanpa memperhatikan urutan.
# Rumus kombinasi: C(n, k) = n! / (k! * (n - k)!)
# Di sini, n = 14 (total bola), k = 3 (bola yang diambil sekaligus).
# Mengapa menggunakan kombinasi? Karena urutan pengambilan bola tidak penting,
# dan bola dianggap berbeda satu sama lain meskipun ada warna yang sama.
# Hasil perhitungan: C(14, 3) = 14! / (3! * 11!) = (14 * 13 * 12) / (3 * 2 * 1) = 364

# Jumlah bola total
total_bola = 8 + 6  # 8 bola merah + 6 bola biru
bola_diambil = 3

hasil = (total_bola * (total_bola - 1) * (total_bola - 2)) // (bola_diambil * (bola_diambil - 1) * (bola_diambil - 2))

print(f"Jumlah kombinasi bola yang dapat diambil:",hasil)