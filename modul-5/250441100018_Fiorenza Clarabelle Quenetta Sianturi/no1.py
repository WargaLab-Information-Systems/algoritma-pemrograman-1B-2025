def faktorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
    
n = int(input("masukkan angka: "))
if n < 0:
    print("faktorial tidak terdefinisi untuk bilangan negatif")
elif n == 0 or n == 1:
    print(f"faktorial dari {n} adalah 1")
else:
    print(f"faktorial dari {n} adalah", faktorial(n))