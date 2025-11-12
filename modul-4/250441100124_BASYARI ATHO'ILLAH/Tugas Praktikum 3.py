n = int(input("Masukkan tinggi piramida (n): "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
        
    for k in range(2 * (n - i)+2):
        print(" ", end="")

    for l in range(i, 0, -1):
        print(l, end="")

    print() 


