motor_matic = 50000
motor_trail = 100000
motor_sport = 75000
print("selamat datag di rental aconk, silahkan pilih ingin menyewa motor apa!")

pilih_motor = input("pilih motor yang di sewa : ")
harga = input("masukkan harga rental : ")
sewa = int(input("masukkan berapa hari ingin sewa : "))
kupon = input("masukkan kode kupon :")

hari = 3
subtotal = 0
biaya = 0

subtotal = harga * hari
print(subtotal)

while True :
    if sewa > hari :
        asuransi = 15000
    elif subtotal > 150000 :
        diskon = 10
    else :
        kupon = input("masukkan kode kupon :")
    if kupon == "aconkGG" :
        diskon = 5
    biaya = subtotal - (subtotal // 100 )
    print(f"biaya yang harus dibayar{biaya}")
    
    lanjut = input("apa ada yang ingin menyewa lagi (ya/tidak)")
    if lanjut == "ya" :
        break

