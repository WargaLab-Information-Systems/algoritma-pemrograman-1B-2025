print("Analisis kalimat")
kalimat = input("Masukkan kalimat: ")

vokal = "aiueo"
jml_vokal = 0
jml_konsonan = 0
jml_kata = 1  

for huruf in kalimat:
    if huruf != ' ':
        if huruf.isalpha():
            if huruf in vokal:
                jml_vokal += 1
            else:
                jml_konsonan += 1
    else:
        jml_kata += 1 

print("Jumlah huruf vokal:", jml_vokal)
print("Jumlah huruf konsonan:", jml_konsonan)
print("Jumlah kata:", jml_kata)