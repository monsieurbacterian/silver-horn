class Backpack:

    def __init__(self, gift=None): #gift=None это значение по умолчанию, которого может и не быть
        self.content = []
        if gift: # тоже самое, что и gift == True и gift != None
            self.content.append(gift)

    def __add__(self, other):
        new_object = Backpack()
        new_object.content.extend(self.content)
        new_object.content.extend(other.content)
        return new_object
        
    def __str__(self):#меняет вывод данных с непонятного на задаваемый нами
        return 'Backpack: ' + ', '.join(self.content)#заданный нами вывод

    def __len__(self):
        return len(self.content) #теперь len считает длину через кол-во слов в списке

    def _bool__(self): #меняет функцию true/false
        if self.content != []:
            return True
        else:
            return False
        
    def add(self, item):
        #положить в рюкзак
        self.content.append(item)
        print('В рюкзак положили:', item)


my_backpack = Backpack('флешка')
my_backpack.add('книга')

his_backpack = Backpack('телефон')
his_backpack.add('ноутбук')
his_backpack.add('зарядка для ноута')

print(len(my_backpack)) # длинну будет выдавать если изменить функцию len 
print(his_backpack)

new_backpack = my_backpack + his_backpack
print(new_backpack)

if my_backpack:
    print('True')
else:
    print('False')
