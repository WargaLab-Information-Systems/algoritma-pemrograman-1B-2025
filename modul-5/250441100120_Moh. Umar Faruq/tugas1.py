
def faktorial(N):
    
    if N == 0 or N == 1:
        return 1
    else:
        
        return N * faktorial(N - 1)


N = int(input("Masukkan bilangan bulat non-negatif: "))

if N < 0:
    print("Maaf, faktorial tidak terdefinisi untuk bilangan negatif.") 
else:
    hasil = faktorial(N)
    print(f"Faktorial dari {N} adalah {hasil}")
