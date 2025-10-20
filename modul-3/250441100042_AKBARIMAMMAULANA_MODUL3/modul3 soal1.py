# Program menampilkan bilangan prima dari 1 sampai n

n = int(input("Masukkan batas angka (n): "))

print(f"Bilangan prima dari 1 sampai {n}:")
for i in range(2, n + 1):
    prima = True
    for j in range(2, int(i ** 0.5) + 1): #digunakan untuk menguji i habis di bagi bilangan lain 
        # jika iya berarti bukan bilangan prima
        if i % j == 0:
            prima = False
            break
    if prima:
        print(i,end=" ")