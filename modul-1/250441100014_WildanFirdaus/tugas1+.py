buku = 5000
pensil = 4500
pajak = 10 #persen

tumbas3_buku = buku * 3
tumbas2_pensil = pensil * 2

total_belanja = tumbas3_buku + tumbas2_pensil
pajak_belanjaan = total_belanja // pajak 

print("total harga membeli 3 buku : ", tumbas3_buku, "rupiah")
print("total harga membeli 2 pensil : ", tumbas2_pensil, "rupiah")
print("pajak yang di dapet oleh halim : ", pajak_belanjaan)
total = (tumbas3_buku + tumbas2_pensil + pajak_belanjaan)

print("jadi total semua harga buku dan pensil halim setelah mendapatkan pajak : ", total)