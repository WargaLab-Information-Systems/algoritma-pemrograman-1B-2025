n = int(input("Masukkan angka : "))

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)
    
hasil = faktorial(n)
if n == 0:
    print(f"Faktorial {n} adalah {hasil} ")
elif n < 0:
    print(f"Bilangan tidak boleh kurang dari 0 maupun bernilai negatif ")
else:
    print(f"Faktorial dari {n}! adalah {hasil}")