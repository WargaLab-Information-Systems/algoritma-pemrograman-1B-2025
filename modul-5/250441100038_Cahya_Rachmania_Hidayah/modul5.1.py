def faktorial(n):
    if n == 0 or n == 1:
        return 1
    if n < 0:
        return "bilangan tidak valid"
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan bilangan bulat non-negatif: "))
print("Hasil faktorial dari", n, "adalah:", faktorial(n))