
n = int(input("Masukkan batas angka (n): "))

print("Bilangan prima dari 1 sampai", n, "adalah:")

for i in range(2, n + 1):
    bilangan_prima = True
    for j in range(2, i):
        if i % j == 0:
            bilangan_prima = False
            break
    if bilangan_prima:
        print(i, end=" ")
