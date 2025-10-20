print("Menghitung Berapa Uang Yang Harus Hallim Bayar Ke Kasir")

 # data barang
harga_buku = 5000
jumlah_buku = 3
harga_pensil = 4500
jumlah_pensil = 2
pajak = 0.10

 # hitung total harga buku dan pensil
total_harga_buku = (harga_buku * jumlah_buku)
total_harga_pensil = (harga_pensil * jumlah_pensil)
total_harga_buku_dan_pensil = (total_harga_buku + total_harga_pensil)
print(f"Total harga buku: Rp, {harga_buku * jumlah_buku} ") 
print(f"Total harga pensil: Rp, {harga_pensil * jumlah_pensil} ")
print(f"Total harga buku dan pensil: Rp, {total_harga_buku_dan_pensil} ")

 # hitung pajak
total_pajak = (total_harga_buku_dan_pensil * pajak)
print(f"Pajak 10%: Rp, {total_pajak} ")

 # hitung total bayar
total_bayar = total_harga_buku_dan_pensil + total_pajak
print(f"Total yang harus dibayar: Rp, {total_bayar} ") 