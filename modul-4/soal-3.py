print("Pola Piramida Cermin")
n = int(input("Masukkan angka n: "))

for i in range(n, 0, - 1):

    for j in range(1, i + 1):
        print(f"{j:2}", end=" ")

    for k in range((n - i) * 6):  
        print(" ", end="")

    for j in range(i, 0, - 1):
        print(f"{j:2}", end=" ")
    print()