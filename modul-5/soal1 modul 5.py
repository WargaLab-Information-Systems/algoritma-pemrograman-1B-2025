def faktorial (n):
    if n == 0 or n == 1 :
        return 1 
    else :
        return n * faktorial (n-1)
    
n = int(input("Masukkan bilangan : "))

if n < 0 :
    print("Bilangan harus non-negatif! ")
else:
    hasil = faktorial(n)
    print(f"Hasil faktorial dari {n}! = {hasil}")
    