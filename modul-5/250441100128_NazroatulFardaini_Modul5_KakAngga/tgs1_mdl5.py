def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
n = int(input("masukkan angka: "))
print(f"faktorial dari {n} adalah {faktorial(n)}")