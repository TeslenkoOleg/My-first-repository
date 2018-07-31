person1 = input("Выберите персонажа которым будете сражаться:")
person2 = input("Выберите врага(орк, эльф, гоблин):")
print("Ваш враг -  "+person2+".")
print("У него 3 жизни!")
print(person1+", Вы должны убить " + person2 + "а !")
health = 3



def hit():
    global health, person2, person1

while health != 0:



    kick=input("Напишите 'ударить':")
    if kick == "ударить":
           health -=1
           if health > 0:
              print("Вы отняли у "+person2+"а одну жизнь.")
              print("У "+person2+"а еще "+str(health)+" жизни.")
           else:
               print(person2+" погибает!")
               print("Поздравляем!"+person1+", ты победил "+person2+"а !")
    else:
        print("Неверный прием!")


   # else:
        #

hit()




hit()