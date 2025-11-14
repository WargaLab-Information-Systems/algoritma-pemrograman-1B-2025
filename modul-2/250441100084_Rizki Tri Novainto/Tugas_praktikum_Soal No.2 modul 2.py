#soal nomer 2
tiket = 50000

hari = (input("Masukkan hari: "))
usia = int(input("Masukkan usia: "))
status_pelajar = input("Apakah SMA? (ya/tidak): ")


if usia < 12:
    total = tiket - (tiket * 50 // 100)   
elif status_pelajar == "ya":
    total = tiket - (tiket * 30 // 100)   
elif hari == "Selasa":
    total = tiket - (tiket * 20 // 100)   
else:
    total = tiket                         

print()
print("Total harga tiket yang harus dibayar: Rp.", total) 
