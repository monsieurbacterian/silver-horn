from random import randint, choice #рандомазер чисел


class Man:

    def __init__(self, name, home):
        self.name = name
        self.fullnes = 50
        self.home = home
        self.eat_counter = 0
        self.fingers = 10
        self.play_counter = 0
        self.work_counter = 0
        self.shopping_counter = 0
        self.clean_counter = 0
##        self.food = 20
##        self.money = 30
        
    def __str__(self):
        return f'{self.name}, моя сытость {self.fullnes}'

    def shopping(self):
        if self.home.money >= 40:
            self.home.money -= 40
            self.home.food +=40
            self.shopping_counter += 1
            print(f'{self.name} ходил в магазин')
        else:
            print('Денег нет!')

    def check_dirt(self):
        if self.home.dirt >=60:
            self.clean()


    def clean(self):
        if self.fullnes <= 20 and self.home.dirt >= 60:
            sel.eat()
            self.home.dirt -= 60
            self.fullnes -= 20
            print(f'{self.name} очистил дом от грязи')
            self.clean_counter += 1
        else:
            self.home.dirt -= 60
            self.fullnes -= 20
            print(f'{self.name} очистил дом от грязи')
            self.clean_counter += 1
            
    def eat(self):
        if self.home.food >= 10:
            self.fullnes += 10
            self.home.food -= 10
            self.eat_counter += 1
            print(f'{self.name} поел')
        else:
            print('Еды нет!')
            
    def play_WoT(self):
        self.fullnes -= 10
        self.play_counter += 1
        print(f'{self.name} поиграл в WoT')

    def work(self):
        self.home.money += 40
        self.fullnes -= 30
        self.work_counter += 1
        print(f'{self.name} поработал')
        
    def year_results(self):
        print(f'{self.name} ел {self.eat_counter}, играл {self.play_counter}, ходил в магазин {self.shopping_counter}, работал {self.work_counter}, осталось пальцев {self.fingers}, очистил дом от грязи {self.clean_counter} раз')

    def act(self):
        if self.fullnes <= 0:
            print(f'{self.name} уехал на лечение')
            return
        
        dice = randint(1, 6)#рандомное число в интеравле 1-6
        if self.fullnes <= 30:
            self.eat()
        elif self.home.food <= 80:
            self.shopping()
        elif self.home.money <= 100:
            self.work()
        elif self.home.dirt > 60:
            self.clean()
        else:
            #print(dice, '--', self.name)
            if dice in [1]:
                self.eat()
            elif dice in [3]:
                self.work()
            else:
                self.play_WoT()
        

class Cat:

    def __init__(self, name, home):
        self.name = name
        self.fullnes = 30
        self.home = home
        self.eat_counter = 0
        self.murrr_counter = 0
        self.fingers_counter = 0
        self.dirt_counter = 0
        self.finger_restored_counter = 0
        self.sleep_counter = 0

        
    def __str__(self):
        return f'Я кот {self.name}, моя сытость {self.fullnes}'

    def eat(self):
        if self.home.food >= 10:
            self.fullnes += 20
            self.home.food -= 10
            self.eat_counter += 1
            print(f'{self.name} поел')
        elif self.fullnes >= 90:
            print('Барсик сейчас лопнет')
            self.murrr()
        else:
            print('Еды нет!')

    def sleep(self):
        self.fullnes -= 5
        self.sleep_counter += 1

    def make_dirt(self):
        self.home.dirt += 5
        self.fullnes -= 10
        self.dirt_counter += 1
        print(f'Уровень грязи увеличился -- {self.home.dirt}')

    def murrr(self):
        person = choice(people)
        person.fullnes += 5
        self.fullnes -= 5
        if person.fingers < 10:
            person.fingers +=1
            self.finger_restored_counter += 1
        self.murrr_counter += 1
        print(f'Кот {self.name} помурлыкал, {person.name} воодушевился')
        
    def act(self):
        if self.fullnes <= 0:
            person = choice(people)
            if person.fingers >= 8:
                person.fingers -= 1
                self.fingers_counter += 1
                person.fullnes -= 5
                self.fullnes += 15
                self.make_dirt()
                print(f'{self.name} откусил палец жильцу {person}')
            else:
                print(f'{self.name} пропал без вести')
            return
        elif self.fullnes >= 30:
            dice = randint(1, 6)
            if dice in [1, 2]:
                self.eat()
                self.sleep()
                print('Барсик поел')
            elif dice in [3, 4]:
                self.make_dirt()
            else:
                self.murrr()
                self.make_dirt()
                print('Барсик помурлыкал')

        elif self.fullnes <= 20:
            self.eat()
            self.sleep()
            print('Барсик поел')
        else:
            self.make_dirt()
            print('Барсик насвинячил')

           
    def year_results(self):
        print(f'{self.name} ел {self.eat_counter} раз, мурлыкал {self.murrr_counter}, откусил пальцев {self.fingers_counter}, насвинячил {self.dirt_counter}, восстановил пальцев {self.finger_restored_counter}, поспал {self.sleep_counter}')


class House:

    def __init__(self):
        self.food = 80
        self.money = 80
        self.dirt = 0

    def __str__(self):
        return f'В доме запас еды {self.food}, деньги {self.money}, уровень грязи {self.dirt}'


berloga = House()
vasya = Man(name='Вася', home=berloga)
petya = Man(name='Петя', home=berloga)
jura = Man(name='Юра', home=berloga)
people = [vasya, petya, jura]
barsik = Cat(name='Барсик', home=berloga)
azoth = Cat(name='Азот', home=berloga)

for i in range(1, 366):
    print(f'==========День{i}==========')
    vasya.act()
    petya.act()
    jura.act()
    barsik.act()
    azoth.act()
    print(vasya)
    print(petya)
    print(jura)
    print(barsik)
    print(azoth)
    print(berloga)

vasya.year_results()
petya.year_results()
jura.year_results()
barsik.year_results()


 
    
    
