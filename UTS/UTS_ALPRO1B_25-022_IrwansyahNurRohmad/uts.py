print("Rental Motor Aconk Menyediakan 3 pilihan jenis motor dengan harga sewa :")
print("1. Motor matic : Rp 50000")
print("2. Motor Trail : Rp 100000")
print("3. Motor Sport : Rp 75000")


pilih = input("1/2/3 :")


matic = 50000
trail = 100000
sport = 75000
asuransi = 15000 
diskon = 10
diskon_tambahan = 5
kupon = "AconkGG"
sewa = 0
total = 150000
sewa_per_hari = 0

if matic :
    matic = 1
    print("Total harga Rp50000")

if trail :
        trail = 2
        print("Total harga Rp100000")
if sport :
     sport = 3 
     print ("Total Harga Rp75000")

input("mau sewa berapa hari?")

if sewa > 3 :
    sewa = asuransi
    print("kau mendapatkan asuransi")

if total > 150000:
    diskon = total * 10 / 100
    
