# #nomer 1
# buku_tulis = 5000
# pensil = 4500
# jumlah_pensil = 2
# jumlah_buku = 3
# pajak = 0.10
# # sebelum pajak 
# total_harga_buku = buku_tulis * jumlah_buku
# total_harga_pensil = pensil * jumlah_pensil
# total_semuanya = total_harga_buku + total_harga_pensil
# #setelah pajak
# total_semuanya_setelah_pajak = total_semuanya * pajak
# print("pajak dari total semua barang adalah :" , total_semuanya_setelah_pajak)
# print("jadi halim harus membayar uang sebesar : Rp.",total_semuanya_setelah_pajak + total_semuanya ,"kekasir setelah ditambahkan pajak")

# #Nomor 2
# panjang = int(input("Masukkan panjang : "))
# lebar = int(input("Masukkan lebar : "))
# tinggi = int(input("Masukkan tinggi : "))

# print("luas balok adalah : ", 2 * ((panjang * lebar)+(panjang * tinggi)+(lebar * tinggi)))
# print("volume balok adalah : ", panjang * lebar * tinggi)

#Nomor 3
# fungsi faktorial 

def faktorial(n):
    hasil = 1
    for a in range(1, n+1):
        hasil = hasil * a   
    return hasil

# fungsi kombinasi
def kombinasi(n, r):

    return  faktorial(n) // (faktorial(r) * faktorial(n - r))

# jumlah bola merah, biru, dan jumlah yang diambil
bola_merah = 8 
bola_biru = 6
total_bola = bola_merah + bola_biru
jumlah_diambil = 3

# hitung banyak kombinasi
hasil = kombinasi(total_bola, jumlah_diambil)

print("Jumlah kemungkinan kombinasi bola yang dapat diambil =", hasil)
