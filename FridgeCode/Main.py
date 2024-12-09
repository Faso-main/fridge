import os
from Classes import Fridge

fridge = Fridge() #Создаём холодильник

def main():
    print("Холодос 3000")
    while(True): #Такую конструкцию можно было бы вставить в каждом case, пока не введут правильные значения, но решил сделать просто выход из case
        try:
            max= int(input("Введите размер холодильника: ")) #Задаём максимальный размер холодильника. Можно бы дать возможность менять его после, но решил так
            Fridge.setMax(max)
            break
        except:
            print("Введено не число")
            continue
    mainmenu()

def mainmenu():
    os.system('cls') #Должен очищать поле, но работает только в командной строке
    print("1- Добавить полку \n"
          "2- Добавить продукты на полку\n"
          "3- Впихнуть продукты в холодильник\n"
          "4- Убрать продукт с полки\n"
          "5- Уничтожить полку\n"
          "6- Продукты на полке\n"
          "7- Все продукты\n"
          "8- Клининг\n"
          "9- Закрыть холодильник")
    match(int(input())):
            case 1:
                fridge.addShelf()
                mainmenu()
            case 2:
                if not Fridge.empty(): #Можно было бы вставлять ещё try для получения правильных данных здесь, а не внутри функции. Или while
                    mainmenu()
                i = input("На какую полку?")
                name = input("Название продукта: ")
                num = input("Количество: ")
                fridge.addToShelf(i, name, num)
                mainmenu()
            case 3:
                if not Fridge.empty():
                    mainmenu()
                name = input("Название продукта: ")
                num = int(input("Количество: "))
                fridge.addToSomewhere(name,num)
                mainmenu()
            case 4:
                if not Fridge.empty():
                    mainmenu()
                i = input("С какой полки? ")
                st = input("\nНазвание продукта: ")
                num = input("\nКоличество продукта: ")
                fridge.removeFromShelf(i,st,num)
                mainmenu()
            case 5:
                if not Fridge.empty():
                    mainmenu()
                i = input("Введите номер полки: ")
                fridge.delShelf(i)
                mainmenu()
            case 6:
                if not Fridge.empty():
                    mainmenu()
                i = input("Введите номер полки: ")
                fridge.showShelf(i)
                mainmenu()
            case 7:
                if not Fridge.empty():
                    mainmenu()
                fridge.showFridge()
                mainmenu()
            case 8:
                if not Fridge.empty():
                    mainmenu()
                fridge.cleaning()
                mainmenu()
            case 9:
                raise SystemExit #Завершает программу
            case _:
                print("Такого числа нет")
                mainmenu()

if __name__=='__main__':
    main()
