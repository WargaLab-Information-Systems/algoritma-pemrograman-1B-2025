harga_tiket = 5000 #Rp50.000
umur = int(input("Masukkan umur kamu:"))
status_pelajar = str(input("Apakah anda pelajar SMA? (iya/tidak):"))
hari = str(input("Masukkan hari: "))
diskon = 0
if umur < 12:
    if 50> diskon:
        diskon = 50

if status_pelajar == "iya":
    if 30> diskon:
        diskon = 30

if hari == "selasa":
    if 20> diskon:
        diskon = 20
harga_diskon = harga_tiket -(harga_tiket * diskon/100)
print("harga tiket yang mau di bayar: Rp")
int(harga_diskon), "(diskon yang akan didapatkan adalah", diskon, "%)"
