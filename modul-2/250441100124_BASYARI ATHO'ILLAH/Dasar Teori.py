

# nama = "python"
# if nama ==  "python":
#     print("Hallo " + nama)

# Kunci = "Python"
# password = input("Masukkan password")
# if password == Kunci:
#     print("Password benar")
# else:
#     print("Password Salah")

# #Program Perintah if-elif-else
# angka = int(input("Masukkan sebuah bilangan : "))
# if angka > 0:
#     print("Angka merupakan bilangan positif")
# elif angka < 0:
#     print("Angka merupakan bilangan negatif")
# else:
#     print("Angka merupakan 0")


# #Program if bersarang
# x = int(input("Masukkan nilai x="))
# y = int(input("Masukkan nilai y="))
# if x == y :
#     print("nilai", x, "dan", y, "mempunyai nilai yang sama")
# else:
#     if x > y:
#         print(x, "Lebih besar dari", y)
#     if x < y:
#         print(x, "Lebih kecil dari", y)

# nomor_acak = 7

# print('tebak nomor acak dari 1 - 10')
# tebakan = int(input('Tebakan anda (bil bulat): '))

# if tebakan == nomor_acak:
#     print('Selamat! tebakan anda benar')
#     print('tapi tidak ada hadiah untuk anda :(')
# elif tebakan < nomor_acak:
#     print('tebakan anda terlalu kecil')
# else:
#     print('tebakan anda terlalu besar')

# print('selesai')

# a = int(input("Masukkan umur: "))

# if a <= 15:
#     print("Muda")
# elif a <= 20:
#     print("Remaja")
# else:
#     print("Tua")

# # Program cek ganjil genap
# nilai = int(input("Masukkan angka: "))

# if nilai % 2:
#     print("Bilangan ganjil")
# else:
#     print("Bilangan genap")

# Program angka ke kata
# a = int(input("Masukkan angka (0-9): "))

# if a == 0:
#     print("Angka anda nol")
# elif a == 1:
#     print("Angka anda satu")
# elif a == 2:
#     print("Angka anda dua")
# elif a == 3:
#     print("Angka anda tiga")
# elif a == 4:
#     print("Angka anda empat")
# elif a == 5:
#     print("Angka anda lima")
# elif a == 6:
#     print("Angka anda enam")
# elif a == 7:
#     print("Angka anda tujuh")
# elif a == 8:
#     print("Angka anda delapan")
# elif a == 9:
#     print("Angka anda sembilan")
# else:
#     print("Angka anda not found")


# ipk = 3.50

# if ipk >= 3.75:
#     print("Predikat: Cumlaude")
# elif ipk >= 3.00:
#     print("Predikat: Sangat Memuaskan")
# elif ipk >= 2.50:
#     print("Predikat: Memuaskan")
# else:
#     print("Predikat: Kurang") 

#Soal nomor 5 Modul II
jenis = input("Masukkan Jenis Kendaraan (mobil/truk kecil/truk besar) :")
bayar = input("tunai / e-money: ")
jam = int(input("Masukkan Jam Masuk Tol (0-23): "))
if jenis == "mobil":
    tarif = 15000
elif jenis == "truk kecil":
    tarif = 25000
elif jenis == "truk besar":
    tarif = 40000
else:
    tarif = 0

if bayar == "e-money":
    if jam >= 23 or jam <= 5:
        diskon = 0.2
    else:
        diskon = 0.1
else:
    diskon = 0  
total = tarif - (tarif * diskon)
print("Tarif Normal: ", tarif)
print("Diskon: ", diskon * 100, "%")
print("Total biaya: ", int(total))


