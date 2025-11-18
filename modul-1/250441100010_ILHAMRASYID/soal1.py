buku = 5000
pensil = 4500
pajak = 10 #persen

membeli3_buku = buku * 3
membeli2_pensil = pensil * 2

total_belanja = membeli3_buku + membeli2_pensil
pajak_belanjaan = total_belanja // pajak

print("total harga memebeli 3 buku : ", membeli3_buku, "rupiah")
print("total harga membeli 2 pensil : ", membeli2_pensil, "rupiah")
print("pajak yang di dapat oleh halim : ", pajak_belanjaan)
total = (membeli3_buku + membeli2_pensil + pajak_belanjaan)

print("jadi total semua harga buku dan pensil halim setelah mendapatkan pajak : ", total)