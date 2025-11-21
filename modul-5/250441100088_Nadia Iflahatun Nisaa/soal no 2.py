def cek_anagram(kata1, kata2):
    bakruf1 = 0   
    for _ in kata1:
        bakruf1 += 1

    bakruf2 = 0
    for _ in kata2:
        bakruf2 += 1

    if bakruf1 != bakruf2:
        return False
    
    for huruf in kata1:
        jumruf1 = 0
        jumruf2 = 0

        for h in kata1:
            if h == huruf:
                jumruf1 += 1
        for h in kata2:
            if h == huruf:
                jumruf2 += 1

        if jumruf1 != jumruf2:
            return False
        if kata1 == kata2:
            return False
        return True
kata1 = input("masukkan kata petama:")
kata2 = input("masukkan kata kedua:")

if cek_anagram(kata1, kata2):
    print("kedua kata termasuk anagram")
else:
    print("keduanya bukan anangram")
        
    