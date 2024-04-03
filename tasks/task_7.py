word = str(input())
sgl = 0
gl = 0 
for i in word:
    letr = i.lower()
    if (letr == "а") or (letr == "е") or (letr == "и") or (letr == "ы") or (letr =="я") or (letr == "ё") or (letr == "ю") or (letr == "э") or (letr == "о"):
        gl += 1
    else:
        sgl += 1

print(f"Гласных - {gl} \n Согласных - {sgl}")