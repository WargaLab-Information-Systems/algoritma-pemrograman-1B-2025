def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Masukkan bilangan bulat non-negatif: "))

if n < 0:
    print("Faktorial tidak dapat dihitung untuk bilangan negatif.")
else:
    print("Faktorial dari", n, "adalah:", factorial(n))