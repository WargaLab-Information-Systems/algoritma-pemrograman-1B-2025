kalimat = input("Masukkan sebuah kalimat: ")

huruf_vokal = 0
huruf_konsonan = 0
jumlah_kata = 1

for huruf in kalimat:
        if huruf == " ":
           jumlah_kata = jumlah_kata + 1
        elif huruf in "aiueoAIUEO":
            huruf_vokal = huruf_vokal + 1
        elif huruf != " ":
             huruf_konsonan = huruf_konsonan + 1

print("Banyak huruf vokal :", huruf_vokal)
print("Banyak huruf konsonan :", huruf_konsonan)
print("Banyak jumlah kata :", jumlah_kata)