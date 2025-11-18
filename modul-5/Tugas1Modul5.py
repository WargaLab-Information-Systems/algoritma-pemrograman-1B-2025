# Fungsi rekursif untuk menghitung faktorial
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

angka = int(input("Masukkan bilangan bulat non-negatif: "))
if angka < 0:
    print("Maaf, hanya bilangan non-negatif yang diperbolehkan.")
else:
    print(f"Faktorial dari {angka} adalah: {faktorial(angka)}")
