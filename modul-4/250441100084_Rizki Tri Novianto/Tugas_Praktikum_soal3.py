
n = int(input("Masukkan jumlah baris: "))
lebar = len(str(n)) + 1  # lebar tetap per angka

for i in range(n, 0, -1):
    # kiri
    for j in range(1, n - i + 2):
        print(" " * (lebar - len(str(j))) + str(j), end="")

    # tengah
    print(" " * ((i - 1) * lebar * 2), end="")

    # kanan
    for j in range(n - i + 1, 0, -1):
        print(" " * (lebar - len(str(j))) + str(j), end="")

    print()









# n = int(input("Masukkan jumlah baris: "))
# # untuk membentuk pola
# for i in range (n , 0 , -1):
#     # mencetak dari angka 1 sampai n-i+1 (bagian kiri)
#     for j in range (1, n - i + 2):
#         print(j, end="")
#     # mencetak spasi di tengah (i-1)*2

#     for k in range ((i - 1)*2):
#         print(" ",end="")
#     # mencetak dari angka n-i+1 sampai 1 (bagian kanan)

#     for s in range (n - i + 1, 0 , -1):
#         print(s,end="")
#     print()