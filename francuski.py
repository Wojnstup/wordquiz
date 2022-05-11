from random import shuffle
words = [
    ("lunettes","okulary"),
    ("un manteau","plaszcz"),
    ("un pull","sweter"),
    ("un jupe","spodnica"),
    ("des collants","rajstopy"),
    ("des bottes","buty"),
    ("un bonnet","kapelusz"),
    ("une echarpe","szalik"),
    ("des gants","rekawice"),
    ("un anorak","anorak"),
    ("un blouson","kurtka"),
    ("un tee-shirt","T-shirt"),
    ("un jean","jeansy"),
    ("des baskets","tenisowki"),
    ("une veste","kamizelka"),
    ("une cravate","krawat"),
    ("une chemise","koszula"),
    ("un costume","garnitur"),
    ("une ceinture","pas"),
    ("un pantalon","spodnie od garnituru"),
    ("des chaussures","lakierki")
]

shuffle(words)

score = 0
for pair in words:
    choice = input(pair[1] + " - ")

    if choice == pair[0]:
        score += 1
        print("Correct!")
    else:
        print("Wrong! Correct answer: " + pair[0])

print("Score: " + str(score) + "/" + str(len(words)))
