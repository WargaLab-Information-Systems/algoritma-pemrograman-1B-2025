def cek_anagram(kata1, kata2):
  
    kata1 = kata1.lower()
    kata2 = kata2.lower()

    if len(kata1) != len(kata2):
        return False

 
    for huruf in kata1:
        
        jumlah1 = 0
        jumlah2 = 0

        
        for h1 in kata1:
            if h1 == huruf:
                jumlah1 += 1

        
        for h2 in kata2:
            if h2 == huruf:
                jumlah2 += 1

        
        if jumlah1 != jumlah2:
            return False

    
    return True



kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

hasil = cek_anagram(kata1, kata2)

if hasil:
    print(f"'{kata1}' dan '{kata2}' adalah anagram.")
else:
    print(f"'{kata1}' dan '{kata2}' bukan anagram.")
