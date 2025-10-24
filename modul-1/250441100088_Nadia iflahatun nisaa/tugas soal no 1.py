#SOAL NO 1

#harga satuan
satu_buku = 5000
satu_pensil = 4500

#jumlah barang
banyak_buku = 3
banyak_pensil = 2

#total before pajak
total_semua= (satu_buku * banyak_buku) + (satu_pensil * banyak_pensil)
print("total before pajak : rp", total_semua)

#pajak
pajak = total_semua * 0.10
print("pajak (10%) : rp", pajak)

#total bayar
total_dibayar = total_semua + pajak
print("total yang perlu dibayar : rp", total_dibayar)


