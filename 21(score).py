koloda = [6,7,8,9,10,11,2,3,4] * 4
import random
random.shuffle(koloda)
comp_score = 0
hum_score = 0
print("    Начинает компьютер:")
print("")
while True:
    mix = koloda.pop()
    print("Ему попалась карта", mix)
    comp_score += mix
    if 16 < comp_score < 21:
        print("У него", comp_score, "очков")
        break
    elif comp_score == 21:
        print("КОМПЬЮТЕР НАБРАЛ РОВНО 21 ОЧКО!!!")
        break
    else:
        if comp_score > 21:
            print("ПЕРЕБОР")
            comp_score = 0
            break
while True:
    print("Будете брать карту? (y/n)")
    choice = input("")
    if choice == "y":
        mix = koloda.pop()
        print("Вам попалась карта", mix)
        hum_score += mix
        if hum_score > 21:
            print("У Вас ПЕРЕБОР")
            hum_score = 0
            break
        elif hum_score == 21:
            print("ВЫ НАБРАЛИ РОВНО 21 ОЧКО!!!")
            break
        else:
            print("У Вас", hum_score, "очков")
    elif choice == "n":
        print("У Вас", hum_score, "очков")
        break
if hum_score < comp_score:
    print("ПОБЕДИЛ КОМПЬЮТЕР")
elif hum_score == comp_score:
    print("ПОБЕДИЛА ДРУЖБА")
else:
    print("ВЫ ПОБЕДИЛИ")
print("Спасибо за игру")