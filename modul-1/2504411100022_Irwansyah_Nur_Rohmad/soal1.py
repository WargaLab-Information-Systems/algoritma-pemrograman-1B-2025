jumlah_buku = 3
harga_buku = 5000
jumlah_pensil = 2 
harga_pensil = 4500
presentase = 10
# total sebelum terkena pajak
total_buku = jumlah_buku * harga_buku
total_pensil = jumlah_pensil * harga_pensil
total = total_buku + total_pensil
pajak = total * presentase / 100
total_yang_dibayar = total + pajak
print(f"\nRincian Belanja Hallim : ")
print(f" - Buku Tulis : {jumlah_buku} * {harga_buku} Rp{total_buku}")
print(f" - Pensil : {jumlah_pensil} * {harga_pensil} Rp {total_pensil}")
print(f"\n total : Rp {total}")
print(f" Pajak : ({presentase}%) : Rp {pajak}")
print(f"\n TOTAL YANG HARUS DIBAYAR : Rp {total_yang_dibayar}")


