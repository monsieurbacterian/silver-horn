f = open('results.txt', encoding='ANSI')
f2 = open('Task 8.txt', 'w', encoding='utf-8')
spisok = []
spisok2 = []
amnt = []
amnt_ann = []
amnt_str = []
names_a = set()
tanya_ann = []
ann = []
newline = '\n'

for line in f: #итерация файла
    item = line.strip().split() #приводим файл в нормальный вид, где каждое слово разделено запятой
    spisok.append(item)#заполняем spisok группами из каждой строки
    for i in item: 
        spisok2.append(i)#заполняем spisok2, где каждое слово записано отдельно
for words in spisok: # итерация по spisok
    digit = int(words[3]) # по каждой строке из списка выделяется только третий символ(цифра)
    digit_str = words[3]
    amnt.append(digit)
    amnt_str.append(digit_str)
    if 'Аня' in words:
        digit_for_ann = int(words[3])
        amnt_ann.append(digit_for_ann)
    if 'Аня' in words:
        ann.append(words)
        if 'Таня' in words:
            ann.remove(words)

    

names_and_numbers = set(spisok2)
amnt_str_set = set(amnt_str)
names = names_and_numbers - amnt_str_set


for name in names:
    if name[-1] == 'а':
        names_a.add(name)


vsego_ballov = f'Всего собрано баллов: {str(sum(amnt))}'
kol_vo = vsego_ballov + str(sum(amnt))#Общая сумма очков

vsego_ballov_ann = f'Команды, в которых участвовала Аня, собрали: {str(sum(amnt_ann))}'
kol_vo_ann = vsego_ballov_ann + str(sum(amnt_ann))#Баллы команд с Аня

vsego_names = f'Участницы: {", ".join(names)} '

vsego_names_a = f'Имена, заканчивающиеся на "а":  {", ".join(names_a)}'

vsego_ann_no_tanya = f'Команды с Аней, но без Тани это:\n {newline.join(", ".join(i) for i in ann)}' # Разделение списков в списке, где первый join разделяет списки в списке,
#а второй join разделяет жлементы списков в списке

result = vsego_ballov, vsego_ballov_ann, vsego_names, vsego_names_a, vsego_ann_no_tanya

print('\n'.join(result))
f2.write('\n'.join(result))
f.close()
f2.close()
