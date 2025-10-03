# Program menghitung total belanja Hallim setelah pajak 10%

# hitung total sebelum pajak
harga_buku = 5000
harga_pensil = 4500
jumlah_buku = 3
jumlah_pensil = 2

total_buku = harga_buku * jumlah_buku
total_pensil = harga_pensil * jumlah_pensil
total_sebelum_pajak = total_buku + total_pensil

print("total sebelum pajak adalah:", total_sebelum_pajak)

# hitung pajak 10%
pajak = 0.10 * total_sebelum_pajak

print("pajak (10%):", pajak)

# hitung total setelah pajak
total_setelah_pajak = total_sebelum_pajak + pajak

print("total yang harus dibayar:", total_setelah_pajak)
