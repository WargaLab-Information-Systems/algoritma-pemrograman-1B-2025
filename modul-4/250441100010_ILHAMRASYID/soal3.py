n = int(input("Masukkan nilai n : "))

for i in range (n , 0 , -1 ) : 
    for j in range (1 , i + 1):
        print(f"{j:>3}", end="")

    for k in range((n - i)* 6):
        print(" ", end="")
    
    for j in range(i, 0, -1):
        print(f"{j:>3}", end="")
    
    print()