harga_normal = 50000 
usia = int(input("Masukkan usia: ")) 
status = input("Apakah anda seorang pelajar dengan kartu pelajar? (ya/tidak): ") 
hari = input("Masukkan hari: ") 
diskon = 0  
# diskon 
if usia < 12: 
 diskon = 50 
elif status == "ya": 
 diskon = 30 
elif hari == "selasa": 
 diskon = 20 
else : 
 print() 
# menghitung harga 
harga_bayar = harga_normal - (harga_normal * diskon // 100) 
print("harga yang harus anda bayar sebesar: ", harga_bayar) 