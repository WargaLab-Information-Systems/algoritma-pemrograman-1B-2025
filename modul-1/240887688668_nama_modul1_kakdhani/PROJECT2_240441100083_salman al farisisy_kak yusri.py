#soal nomer 1
# nama = (input("masukkan nama :"))
# nim = (input("masukkan NIM: "))
# uts = int(input("masukkan nilai UTS:"))
# uas = int(input("masukkan nilai UAS: "))
nilai = int(input("masukkan nilai:"))

# print ("nama anda:", nama)
# print ("nim anda:", nim)
print ("nilai rata-rata anda:", nilai)


if nilai >= 0 and nilai <= 40:
    print("nilai anda e")
elif nilai >= 41 and nilai <=60:
    print("nilai anda d")
elif nilai >= 61 and nilai <=70:
    print("nilai anda c")
elif nilai >= 71 and nilai <=80:
    print("nilai anda b")
elif nilai >= 81 and nilai <=100:
    print("nilai anda a")
else:
    print("nilai anda tidak valid")
    

#soal nomer 2
# skor_jaka = 1000
# ipk_jaka = 3.5

# skor_ida = 11000
# ipk_ida = 3.5

# ipk=3.5
# skor=1100


# if skor_jaka >= skor and ipk_jaka >=ipk:
#     print("jaka lulus")
# else:
#     print("jaka tidak lulus")

# if skor_ida >= skor and ipk_ida >=ipk:
#     print("ida lulus")
# else:
#     print("ida tidak lulus")

# soal nomer 4
# tahun = int(input("Masukkan tahun: "))

# if tahun % 4 == 0:
#     if tahun % 100 == 0:
#         if tahun % 400 == 0:
#             print(f"{tahun} adalah tahun kabisat.")
#         else:
#             print(f"{tahun} bukan tahun kabisat.")
#     else:
#         print(f"{tahun} adalah tahun kabisat.")
# else:
#     print(f"{tahun} bukan tahun kabisat.")

#soal nomer 5
# nama = input("nama pembeli:")
# usia = int (input("masukkan usia anda:"))
# if  usia < 18:
#     print("maaf usia belum mencukupi")
#     exit()

# total_belanja = float(input("masukkan total belanja anda:"))
# member = input("apakah anda memiliki member? iya/tidak:")
# if member == "iya":
#     member = True
# else:
#     member = False
# if total_belanja >= 500000:
#     diskon = 0.10
# else :
#     diskon = 0
# if member:
#         diskon += 0.15

        
# diskon_rupiah = total_belanja * diskon
# total_bayar = total_belanja - diskon_rupiah

# print("nama anda:", nama)
# print("diskon yang anda dapatkan:",diskon* 100, "%" )
# print("total harga sebelum diskon", total_belanja )
# print("total harga anda:", total_bayar)