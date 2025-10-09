usia = int(input("Masukkan usia anda : "))
status_pelajar = input("Apakah pelajar SMA? (ya/tidak): ") 
hari = input("Masukkan hari: ")

# Harga normal
harga_normal = 50000
diskon = 0

# diskon
if usia < 12:
    diskon = 50  
elif status_pelajar == "ya":
    diskon = 30  

if hari == "selasa" or diskon < 20:
    diskon = 20  
    
# Hitung harga 
harga_bayar = harga_normal - (harga_normal * diskon / 100)
print(f"Diskon yang didapat: {diskon}%")
print(f"Harga yang harus dibayar: Rp {int(harga_bayar):,}")