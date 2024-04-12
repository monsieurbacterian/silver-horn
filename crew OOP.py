class Crew:

    def __init__(self):
        self.names = set()
        

    def add(self, name):
        self.names.add(name)

    def __str__(self):
        return ', '.join(self.names)
    
    def __len__(self):
        return len(self.names)

    def __add__(self, other):
        new_team = Crew()
        new_team.names.update(self.names)
##        result = new_team.names.union(other.names)
        result = new_team.names|other.names
        return result

    def __sub__(self, other):
        new_team = Crew()
        new_team.names.update(self.names)
##        result = new_team.names.difference(other.names)
        result = new_team.names - other.names
        return result
    
crew1 = Crew()
crew2 = Crew()

crew1_list = ['Маша', 'Петя', 'Вася']
crew2_list = ['Петя', 'Юра']

for i in crew1_list:
    crew1.add(i)
for i in crew2_list:
    crew2.add(i)

crew3 = crew1 + crew2
crew4 = crew1 - crew2

digit = crew1_list + crew2_list
print(digit)

print(f'Crew4: Состав: {", ".join(crew3)}. Кол-во участников: {len(crew3)} \nCrew4: Состав: {", ".join(crew4)}. Кол-во участников: {len(crew4)}')
