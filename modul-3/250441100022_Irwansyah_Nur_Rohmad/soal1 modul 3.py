n = int(input("masukkan nilai n :"))

print (f"Bilangan Prima yang terdiri dari 1 sampai {n} :")
for i in range(2, n + 1 ):
    prima = True
    for k in range(2, i):
        if i % k == 0 :
            prima = False
            break
    if prima :
        print(i)

            