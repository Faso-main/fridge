import sys #Можно было бы обойтись без него, но maxsize выглядит красивее

#Публичный класс холодильника
class Fridge:
    # Посчитал, что эти значения не имеет смысла делать self
    _max:int = 0 #Максимальный размер полки
    _Counter: set[int]={0} #счётчик
    _Empty:bool = True #Пустой ли холодильник

    def __init__(self)->None:
        self.Shelfs= {} #Словарь номер полки - полка

    @classmethod
    def setMax(cls, max:int )->None:
        Fridge._max=max

    def addShelf(self)->None: #добавить полку
        for i in range(1,sys.maxsize):  # Находим свободно место в холодильинке
            if i not in Fridge._Counter:
                Fridge._Counter.add(i) #занимает в set место i
                M: int =i
                break
        shelf = Fridge._Shelf(int(Fridge._max)) #Создаём значение полки
        self.Shelfs[M]=shelf #Полка получает ключ. Надо бы сделать update тут. Чтобы полки не стояли [2,1], но нет времени
        Fridge._Empty=False #В холодильнике теперь есть полки
        print(f"Полка добавлена {M}")

    def showShelf(self,i:int)->None: #геттер полки
        try:
                if self.Shelfs.get(int(i)) is None: #Если такой полки нет
                    print("Такой полки нет")
                    return
                shelf = self.Shelfs.get(int(i)) #получает значение номера полки
                if shelf.getNames(): #проверка на то, пустая ли полка
                    print(shelf)
                else:
                    print("Полка пуста")
                    return
        except KeyError:
            print("Такой полки не существует")
        except ValueError:
            print("Полка-число")

    def showFridge(self)->None: #Пишет, что находится в холодильнике
        for keyFrigde, valueFridge in self.Shelfs.items():
            print(f"\nПродукты на полке {keyFrigde}: ")
            value = valueFridge.getDictor()
            for keyShelf, valueShelf in value.items():
                print(f"{keyShelf}: {valueShelf}, ")

    def nameSum(self)->int: #Возвращает сумму продуктов. Вдруг понадобится ещё
        sum=0
        for value in self.Shelfs.values():
                sum+=value.sum()
        return sum

    def addToShelf(self, i:int, name: str, num: int = 1 )->None: #добавить к продукту на полке
        try:
            get = self.Shelfs.get(int(i)) #Получаем значение полки
            if get is None: #Проверка
                print("Такой полки нет")
                return
            if get.freeSpace()<int(num): #Проверка на место в холодильнике
                print("Мало места")
                return
            get.addToName(str(name),int(num))
            self.Shelfs[int(i)]=get #Меняем значение этой же полки на новое
        except KeyError:
            print("Такой полки не существует")
        except:
            print("Имя должно быть строкой, а количество числом")

    def removeFromShelf(self, i:int, name: str, num: int = 1)->None: #убрать продукт с полки
        try:
            if self.Shelfs.get(int(i)) is None:
                print("Такой полки нет")
                return
            shelf = self.Shelfs.get(int(i))
            shelf.removeFromName(str(name),int(num))
            self.Shelfs[int(i)]=shelf
        except KeyError:
            print("Такой полки не существует")
        except:
            print("Имя должно быть строкой, а количество числом")

    def addToSomewhere(self, name: str, num: int = 1)->None: #добавить продукт в свободное место
        try:
            for key in self.Shelfs: #получаем ключи - номер и значения - полка
                shelf = self.Shelfs.get(key)
                if shelf.freeSpace() >= num: #Проверяем, достаточно ли место полке
                    shelf.addToName(str(name), int(num)) #изначально здесь был self.addToShelf, но повторялся метод freespace
                    self.Shelfs[key]=shelf
                    return
            print("Нет свободного места в холодильнике")
        except:
            print("Имя должно быть строкой, а количество числом")

    def delShelf(self,i:int)->None: #удаляем полку
        try:
            if self.Shelfs.get(int(i)) is None:
                print("Такой полки нет")
                return
            del self.Shelfs[int(i)] #Удаляем значение в классе
            Fridge._Counter.remove(int(i)) #Убираем номер полки из занятых
        except KeyError:
            print("Такой полки не существует")
        except:
            print("Полка - числом")
        if max(Fridge._Counter)==0: #Если полок нет, то делаем холодильник обратно пустым
            Fridge._Empty=True

    def cleaning(self)->None: #Очистка от продуктов: удаляет полки и ставит заново. Нумерация сбивается. Можно было очищать значения внутри shelf
        for i in range(len(self.Shelfs)+1):
            self.delShelf(i+1)
            count:int = i
        for j in range(count):
            self.addShelf()

    @classmethod
    def empty(cls): #Проверка на пустоту в холодильнике
        if Fridge._Empty:
            print("В холодильнике нет полок")
            return #Возвращает None для работы if в основном коде
        else:
            return 1

    #Приватный внутренний класс полки
    class _Shelf:
        #Можно было бы сделать класс продуктов. Чтоб были делимые и неделимые продукты, например
        #Здесь try нет, потому что проверка проходит во внешнем классе
        def __init__(self, max: int, name: str=None, N: int=1)->None: #Можно было не писать вставление name и N, но пусть будет на будущее
            self.max = max #максимальный размер полки
            self.dictor = {} #Здесь ключом является продукт, а значение - количество. Продукт не сможет повторяться на полке. Количество можно было сделать double
            if name is not None:
                if max < N or N < 1:
                    raise ValueError()
                self.dictor[name] = N

        def getNames(self)->list[str]: #Получаем названия продуктов
            names = []
            for key in self.dictor:
                names.append(key)
            return names

        def sum(self)->int: #Сумма продуктов на полке
            sum=0
            for value in self.dictor.values():
                sum+=value
            return sum

        def freeSpace(self)->int: #высчитывает свободное место на полке
            space=self.max
            for value in self.dictor.values(): #Если полка будет пустая, то вернёт self.max в итоге
                space-=value
            return space

        def addToName(self, name: str, num: int = 1)->None: #Добавление продукта или количества к продукту
            if self.dictor.get(name) is None:
                self.dictor[name] = num  # Если продукт не найден, то создаём его
                return
            if self.freeSpace()<(self.dictor.get(name) + num): #Проверка на свободное место, если продукт есть
                return
            else:
                number = self.dictor.get(name) #если продукт есть, то берём его количество и добавляем к уже существующему
                number+=num
                self.dictor[name]=number #Если продукт найден и есть свободное место, добавляем к нему

        def removeFromName(self, name: str, num: int = 1)->None: #Убрать какое-то количество продукта
            full = self.dictor.get(name)
            if num<1 or num>full: #Эту проверку надо бы сделать во внешнем классе, но так легче
                print("Нет столько продуктов")
                return
            full-=num
            self.dictor[name]=full
            if self.dictor.get(name)==0:
                del self.dictor[name] #Удаляет продукт из списка, если его количество=0

        def __str__(self)->str: #Пишет продукты на полке и количество
            Return = ""
            for key in self.dictor:
                Return+= f" Количество {key}: {self.dictor.get(key)}\n"
            return Return
