kalimat = input("Masukan kalimat : ")

vokal = 0
konsonan = 0
angka = 0
kata = 1 

for i in kalimat: 
    if i == " " :  
        kata += 1
    elif (i >= '0' and i <= '9') :
        angka += 1
    elif ( i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') :
        if i in 'aiueoAIUEO': 
            vokal += 1
        else: 
            konsonan += 1
            
print("Jumlah huruf vokal :", vokal)
print("Jumlah huruf konsonan :", konsonan) 
print("Jumlah angka :", angka) 
print("Jumlah kata :", kata) 