#soal no 3
#Meminta input tinggi piramida
n = int(input("Masukkan tinggi piramida (n): "))

for i in range(n, 0 , -1):
    for j in range(1, n - i + 2):  
        print(j, end="")
    
    for k in range((i - 1) * 2):  
        print(" ", end="")
    
    for l in range(n - i + 1, 0, -1):  
        print(l, end="")

    print()
