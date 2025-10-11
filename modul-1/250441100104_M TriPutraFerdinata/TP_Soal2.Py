panjang = int(input("masukan nilai panjang:"))
lebar = int(input("masukan nilai lebar:"))
tinggi = int(input("masukan nilai tinggi:"))

volume_balok = panjang*lebar*tinggi
luas_balok = 2*((panjang*lebar)+(panjang*tinggi)+(lebar*tinggi))

print("volume_balok adalah:", volume_balok)
print("luas_balok adalah:", luas_balok)