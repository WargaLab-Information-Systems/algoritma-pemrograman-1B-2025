# for hari in ["Senin", "Selasa", "Rabu"]:
#     print("Jadwal hari", hari)
#     for pelajaran in ["Matematika", "IPA", "Bahasa Indonesia"]:
#         print("-", pelajaran)
#     print() 

# baris = int(input("Masukkan jumlah baris: "))

# for i in range(1, baris + 1):
#     print(" " * (baris - i), end="")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# # Loop luar (outer loop)
# for i in range(1, 4): # Loop ini akan berjalan 3 kali(i = 1, 2, 3)
#     print(f"loop luar i = {i}")

# # Loop dalam (inner loop)
# for j in range(1, 4): # Loop ini juga akan berjalan 3 kali untuk setiap iterasi dari loop luar
#     print(f" Loop dalam j = {j}")

# a = 24
# b = 36
# while b != 0:
#   a, b = b, a % b
#   print(f"FPB-nya adalah : {a}") 



n = 100 # Batas angka
a, b  = 0, 1

# print("Bilangan fibonacci hingga", n)
# while a <= n:
#    print(a, end=" ")
#    a, b = b, b + a


n = 5

for i in range(1, n+1):
   
    for j in range(n-i):
      print(" ", end=" ")

    for k in range(1, i + 1):
         print(k, end=" ")
    print()


