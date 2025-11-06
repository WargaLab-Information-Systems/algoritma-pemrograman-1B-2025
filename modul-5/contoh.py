# ''' FUNCTION '''

# def penjumlahan(angka1,angka2):
#     hasil = angka1 + angka2
#     return hasil

# input_angka = penjumlahan(5, 6)
# print("Ini adalah hasil penjumlahan :", input_angka)


# # ''' LAMBDA '''
# kuadrat = lambda angka:angka**2

# print("Hasil kuadratnya adalah ",kuadrat(3))

# angka_genap = lambda x : "genap" if x % 2 == 0 else "ganjil"
# print(angka_genap(4))


# '''  FUNGSI REKURSI '''
# def hitung_mundur(n):
#     if n == 0:
#         print("Selesai")
#     else:
#         print("Angka ke :", n)
#         hitung_mundur(n-1)
# hitung_mundur(5)

# def faktorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * faktorial(n-1)
# print("Faktorial dari n adalah", faktorial(5))

# def nama():
#     print("Nama saya adalah Eko Rismanto")

# nama()


''' SCOPE VARIABEL '''
# variabel local dan global

# def sapa():
#     nama = "Nama saya : Eko Rismanto"
#     print(nama)

# sapa()

# variabel global
nama = ""
umur = ""

def sapa_gw():
    nama = "Eko Rismanto"
    umur = 20
    print("Hallo nama saya ", nama, "dan umur saya",umur, "Tahun")

sapa_gw()