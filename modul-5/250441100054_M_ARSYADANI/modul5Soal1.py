def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Masukkan Bilangan bulat non-negatif n: "))
if n < 0:
    print("Error:n harus bilangan bulat non-negatif.")
else:
    hasil = factorial(n)
    print(f"Faktorial dari {n} adalah {hasil}")

