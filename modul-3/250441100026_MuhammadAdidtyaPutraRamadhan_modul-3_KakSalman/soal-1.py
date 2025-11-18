print("Program Bilangan Prima")
n = int(input("Masukkan batas angka: "))

print("Bilangan prima dari 1 sampai", n , ":")
for i in range(2, n + 1):
    jumlah = 0
    for j in range(1, i + 1):
        if i % j == 0:
            jumlah += 1
    if jumlah == 2:
        print(i)