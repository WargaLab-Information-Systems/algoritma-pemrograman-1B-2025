#diketahui jumlah barang
jumlah_buku = 3
jumlah_pulpen = 2
 
#nilai satuan
harga_buku = 5000
harga_pulpen = 4500

#menghitung harga barang
total_harga_buku = (jumlah_buku * harga_buku)
total_harga_pulpen= (jumlah_pulpen * harga_pulpen)

print("Total biaya Buku: Rp", total_harga_buku)
print("Total biaya pulpen: Rp", total_harga_pulpen)

#menghitung harga sebelum dikenakan pajak
harga_asli = total_harga_buku + total_harga_pulpen
print("harga asli: Rp",harga_asli)

#pajak 10%
pajak = harga_asli * 0.10
print("total setelah kena pajakk:",pajak)

#menghitung total biaya setelah dikenakan pajak
total_bayar = pajak + harga_asli
print("Total harga yang harus dibayar: Rp",total_bayar)