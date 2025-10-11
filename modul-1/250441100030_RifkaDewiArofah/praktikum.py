
harga_buku = 5000
harga_pensil = 4500

jumlah_buku = 3
jumlah_pensil = 2

total_buku = harga_buku * jumlah_buku
total_pensil = harga_pensil * jumlah_pensil
total_harga = total_buku + total_pensil

pajak = total_harga * 10

total_bayar = total_harga + pajak

print("Total sebelum pajak: Rp", total_harga)
print("Pajak 10%: Rp", pajak)
print("Total yang harus dibayar: Rp", total_bayar)