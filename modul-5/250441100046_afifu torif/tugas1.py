def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
angka = int(input("masukkan bilangan: "))
hasil = faktorial(angka)
print(f"faktorial dari {angka} adalah {hasil}")
