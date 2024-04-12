import random

hello_answers = ['Салют!', 'Здравствуй!', 'Рад вас видеть!']
bye_answers = ['До новых встречь!', 'Досвидания!', 'Ариведерчи!', 'Bye!']
failure_phrases = ['Я вас не понял, повторите, пожалуйста.', 'Хмммм, немоглибы вы повторить?', 'Я вас не понимаю']

def bot(question):
    if question == 'привет':
        answer = random.choice(hello_answers)
    elif question == 'пока':
        answer = random.choice(bye_answers)
    else:
        answer = random.choice(failure_phrases)
    return answer

print('Бот готов к беседе')
while True:
    question = input()
    if question == 'выход':
        break
    answer = bot(question)
    print(answer)
    
