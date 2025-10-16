print("Masukkan kalimat dan akhiri dengan tanda '-' :")
kalimat = input()
vokal = 0
selainvokal = 0
jkata = 0
dkata = 0 
bangka = 0
bsimbol = 0

for huruf in kalimat:
    if huruf == "-":
        break

    if (huruf >= "a" and huruf <= "z") or (huruf >= "A" and huruf <= "Z"):
        if huruf == "a" or huruf == "i" or huruf == "u" or huruf == "e" or huruf == "o" or huruf == "A" or huruf == "I" or huruf == "U" or huruf == "E" or huruf == "O":
            vokal = vokal + 1
        else:
            selainvokal = selainvokal + 1
            
    elif huruf >= "0" and huruf <= "9":
        bangka = bangka + 1

    elif huruf == "," or huruf == "." or huruf == "!" or huruf == "?" or huruf == ";" or huruf == ":" or huruf == "'" or huruf == '"' or huruf == "-" or huruf == "(" or huruf == ")" or huruf == "[" or huruf == "]" or huruf == "{" or huruf == "}" or huruf == "/" or huruf == "\\" or huruf == "|" or huruf == "`" or huruf == "~" or huruf == "@" or huruf == "#" or huruf == "$" or huruf == "%" or huruf == "^" or huruf == "&" or huruf == "*" or huruf == "_" or huruf == "+" or huruf == "=":
        bsimbol = bsimbol + 1

        if dkata == 0:
            jkata = jkata + 1
            dkata = 1
    else:
        dalam_kata = 0

print("Jumlah huruf vokal:", vokal)
print("Jumlah huruf konsonan:", selainvokal)
print("Jumlah kata:", jkata)
print("Jumlah angka:", bangka)
print("Jumlah simbol:", bsimbol)