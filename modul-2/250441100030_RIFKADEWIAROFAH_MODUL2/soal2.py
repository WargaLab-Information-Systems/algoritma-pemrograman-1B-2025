tiket_normal = 50000

usia = int(input("usia anda sekarang : "))
status = input("Apakah anda pelajar SMA dengan kartu pelajar? (ya/tidak) : ")
nonton_hari = input("Anda nonton hari apa? : ")
diskon = 0

if usia <12 :
    diskon = 50
elif status == "ya":
    diskon = 30
elif nonton_hari == "selasa":
    diskon = 20
else : 
    print()

bayar = tiket_normal - (tiket_normal * diskon // 100)
print("Uang yang anda bayar: ", bayar)