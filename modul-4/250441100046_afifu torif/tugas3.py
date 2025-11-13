n = int(input("Masukkan angka n: "))

for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        print(j, end=" ")
    for k in range(1, (i - 1) * 4 + 1):
        print(" ", end="")
    for l in range(1, n - i + 2):
         print(l, end=" ")   
    print()