n = int(input("Masukkan Nilai N: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")

    for k in range((n - i) * 2 + 2):
        print(" ", end=" ")
    
    for j in range(i, 0, -1):
        print(j, end=" ")
    
    print()