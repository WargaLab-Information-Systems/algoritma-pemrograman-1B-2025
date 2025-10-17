n = int(input("Masukkan Nilai N : "))
print("Bilangan prima dari 1 sampai", n, ":")

for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            Prima = False
            break
    else:
        print(i)