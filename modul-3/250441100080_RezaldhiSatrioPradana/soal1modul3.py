# bilangan_prima=range(1,4)

# for huruf in bilangan_prima :
#     print(range(1,48))
# bilangan_prima=0

# while bilangan_prima <=48 :
#     print(f"bilangan_prima{=+3}")
    

# angka=int(input("masukkan bilangan prima : "))
# print(f"angka sekarang {angka}")

# while angka >=1:    
#     angka +=1
#     print(f"angka sekarang {angka}")
    
# Minta input batas atas (n)


# n = int(input("Masukkan bilangan prima sampai angka (n): "))

# print(f"\nBilangan prima dari 1 sampai {n}:")

# # List untuk menampung hasil
# hasil_prima = []

# # Cek setiap angka, mulai dari 2
# for angka in range(2, n + 1):
#     # Anggap angka ini prima
#     is_prima = True
    
#     # Cek pembagi dari 2 sampai sebelum angka itu
#     # Cek hanya sampai akar kuadrat angka (lebih cepat!)
#     pembagi = 2
#     while pembagi * pembagi <= angka:
#         if angka % pembagi == 0:
#             # Ketemu pembagi lain, jadi BUKAN prima
#             is_prima = False
#             break
#         pembagi += 1
    
#     # Kalau is_prima masih True, masukkan ke list
#     if is_prima:
#         hasil_prima.append(angka)

# # Tampilkan hasilnya
# print(", ".join(str(p) for p in hasil_prima))



# n = int(input("Masukkan batas atas (n) untuk mencari bilangan prima: "))

# print(f"\nBilangan prima dari 1 sampai {n} adalah:")


# hasil_output = ""


# for angka in range(2, n + 1):
    
#     is_prima = True
    
    
#     bagi = 2
#     while bagi * bagi <= angka:
#         if angka % bagi == 0:
            
#             is_prima = False
#             break
#         bagi += 1
    
    
#     if is_prima:
        
#         hasil_output = hasil_output + str(angka) + ", "


# if len(hasil_output) > 0:
#     hasil_output = hasil_output[:-2]


# print(hasil_output)

angka = int(input("Masukkan batas angka: "))

for n in range(2, angka + 1): 
    faktor = 0
    for i in range(1, n + 1):
        if n % i == 0:
            faktor += 1
    if faktor == 2:
        print(n, "adalah bilangan prima")
    