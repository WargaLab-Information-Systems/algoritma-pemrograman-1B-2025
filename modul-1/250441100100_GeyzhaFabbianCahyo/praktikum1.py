# soal ke 1
print("="*50) 
buku_tulis = 5000
pensil = 4500
pajak = 0.10

total_dibayar = (buku_tulis * 3) + (pensil * 2) 
jumlah_pajak = total_dibayar * pajak
dibayar_ke_kasir =  total_dibayar + jumlah_pajak
print("total harus dibayar: ", total_dibayar)
print("setelah dikenai pajak: ", dibayar_ke_kasir)
print("="*50) 
print("\n")
print("\n")

# soal ke 2
print("="*50)
panjang = int(input("Masukan Panjang Nya : "))
lebar = int(input("Masukan Lebar Nya : "))
tinggi = int(input("Masukan Tinggi Nya : ")) 

volume = panjang * lebar * tinggi
luas = 2 * (panjang * lebar) + (panjang * tinggi) + (lebar * tinggi)
print("Volume nya adalah adalah: ", volume)
print("Luas nya adalah: ", luas)
print("="*50) 
print("\n")
print("\n")

# soal ke 3
print("="*50) 
merah = 8
biru = 6
total = merah + biru
ambil = 3

kombinasi = (total * (total - 1) * (total - 2)) // (ambil * (ambil - 1) * (ambil - 2))
print("Jumlah kombinasi bola yang dapat diambil:", kombinasi)
print("="*50)