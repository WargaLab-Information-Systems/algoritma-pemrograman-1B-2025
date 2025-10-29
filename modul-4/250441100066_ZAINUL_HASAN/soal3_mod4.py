n = int(input("Masukkan angka: "))

for i in range(n, 0, -1):  
    for j in range(1, i + 1):
        print(j, end=" ")

    for k in range(1, (n - i) * 2 + 1):
        print(" ", end=" ")
    
    for j in range(i, 0, -1):
        print(j, end=" ")
    print(  )