def faktorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "bilangan tidak valid"
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan bilangan positif: "))
print("Hasil faktorial dari", n, "adalah:", faktorial(n))