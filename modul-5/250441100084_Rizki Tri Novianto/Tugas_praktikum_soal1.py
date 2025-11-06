n = int(input("Masukkan angka: " ))

def faktorial(n):
    if n == -1:
        return 1
    else:
        return n * faktorial(n - 1)

if n == 0:  
    print("Faktorial dari 0 adalah 1")
if n < 0:   
    print("Faktorial tidak terdefinisi untuk bilangan negatif")
else:
    print(f"Faktorial dari {n} adalah {faktorial(n)}")