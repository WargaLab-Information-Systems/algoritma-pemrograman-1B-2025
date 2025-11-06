def faktorial(n):
    if n < 0:
        return "Faktorial tidak bisa dihitung untuk bilangan negatif."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan bilangan bulat positif: "))
print("Hasil faktorial dari", n, "adalah:", faktorial(n))
