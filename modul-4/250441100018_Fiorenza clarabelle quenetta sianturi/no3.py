n = int(input("Masukkan jumlah baris: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if j < 10:
            print(j, end='  ')
        else:
            print(j, end=' ')
    
    for s in range((n - i) * 6):
        print(' ', end='')
    
    for j in range(i, 0, -1):
        if j < 10:
            print(j, end='  ')
        else:
            print(j, end=' ')
    
    print()
