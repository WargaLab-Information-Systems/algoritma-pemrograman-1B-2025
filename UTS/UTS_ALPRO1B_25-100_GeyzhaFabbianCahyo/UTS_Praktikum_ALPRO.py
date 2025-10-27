# while ulang = "ya"

    # motor_matic = 50000
    # motor_trail = 100000
    # motor_sport = 75000
    # hari = int(input("Mau sewa berapa hari :"))

jumlah = int(input("jumlah motor yang mau disewa :"))
motor_disewa = input("Mau sewa motor apa :")
if motor_disewa == "matic" :
    harga = 50000
elif motor_disewa == "trail" :
    harga = 100000
elif motor_disewa == "sport" :
        harga = 75000

subtotal = harga * jumlah

hari = int(input("Mau sewa berapa hari :"))
kupon = input("apakah kamu punya kupon AnconkGG (y/n)")
if kupon == "y" :
        diskon = 0.05
elif subtotal >= 150000 : 
        diskon = 0.10
elif hari >= 3 :
        subtotal -= 15000
else :
        diskon = 0

diskon1 = subtotal * diskon


print()
print(f"lama penyewaan :{hari} hari")
print(f"total motor disewa :{jumlah}")
print(f"harga sewa nya Rp.{subtotal}")
print(f"diskon didapat {diskon * 100}%")
print(f"harga setelah diskon Rp.{diskon1}")