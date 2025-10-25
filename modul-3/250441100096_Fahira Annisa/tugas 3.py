kalimat = input("Masukkan kalimatnya:")

alfabet= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
huruf_vokal = "aiueoAIUEO"
jumlah_huruf_vokal = 0
konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXTZ"
angka = "0123456789"
jumlah_huruf_konsonan = 0
jumlah_kata = 0
jumlah_angka = 0
dalam_kata = False

for huruf in kalimat:
    if huruf in alfabet:
        if huruf in huruf_vokal:
          jumlah_huruf_vokal += 1
        else:
            jumlah_huruf_konsonan += 1 
    elif huruf in angka:
        jumlah_angka += 1

    if huruf != " " and not dalam_kata:
        jumlah_kata += 1
        dalam_kata = True
    elif huruf == " ":
        dalam_kata = False
        

print("jumlah huruf vokal", jumlah_huruf_vokal)
print("jumlah huruf konsonan", jumlah_huruf_konsonan)
print("jumlah angka", jumlah_angka)
print("jumlah kata", jumlah_kata)
