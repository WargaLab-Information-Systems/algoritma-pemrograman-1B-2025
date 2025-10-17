kalimat = input("Masukkan sebuah kalimat: ")

vokal = "aiueoAIUEO"
jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_kata = 1

for i in range(len(kalimat)):
    if kalimat[i] in vokal:
        jumlah_vokal += 1
    elif (kalimat[i] >= 'a' and kalimat[i] <= 'z') or (kalimat[i] >= 'A' and kalimat[i] <= 'Z'):
        jumlah_konsonan += 1
    if kalimat[i] == ' ':
        jumlah_kata += 1

print("Hasil Analisis:")
print("a. Jumlah huruf vokal:", jumlah_vokal)
print("   Jumlah huruf konsonan:", jumlah_konsonan)
print("b. Jumlah kata dalam kalimat:", jumlah_kata)

