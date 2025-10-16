#variabel barang
harga_buku = 5000
harga_pensil = 4500
# menghitung total harga barang sebelum pajak
total_harga_buku = harga_buku*3
total_harga_pensil = harga_pensil*2
total_harga_barang = total_harga_buku+total_harga_pensil
# menghitung pajak pembelian
pajak = 0.10
pajak_pembelian = total_harga_barang*pajak
# menghitung belanja setelah pajak
total_belanja_setelah_pajak = total_harga_barang+pajak_pembelian

print("total harga pensil =", total_harga_pensil)
print("total harga buku =", total_harga_buku)
print("total harga barang =", total_harga_barang)
print("pajak pembelian =", pajak_pembelian)
print("total belanja setelah pajak =", total_belanja_setelah_pajak)