# Program menampilkan bilangan prima dari 1 sampai n
n = int(input("Masukkan nilai n: "))

print("Bilangan prima dari 1 sampai", n, "adalah:")
for i in range(2, n + 1): #mengecek setiap angka dari 2 sampai n
    prima = True
    for j in range(2, i): #memeriksa apakah i habis dibagi oleh bilangan lain dari 2 sampai i-1
        if i % j == 0:
            prima = False
            break
    if prima:
        print(i)