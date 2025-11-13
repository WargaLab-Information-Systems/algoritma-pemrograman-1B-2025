def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
angka = "0123456789"
valid = False

while not valid:
    n = input("masukkan bil.bulat non negatif:")
    valid = True
    for i in n:
        if i not in angka:
            print("masukkan angka yang valid dong!")
            valid = False
            break
n = int(n)
print("faktorial dari", n, "yaitu", faktorial(n))