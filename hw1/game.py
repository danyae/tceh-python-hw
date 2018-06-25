questions = {'Какой язык вы изучаете?': ('python', 'пайтон'),
             'Какая функция выводит текст на экран?': ('print'),
             'Как называется логический тип в Python?': ('bool')
             }

correct = 0
for question in questions:
    answer = input(question + ' ')
    if answer.lower() in questions[question]:
        print('Это верный ответ!')
        correct += 1
    else:
        print('Это неверный ответ!')

print('Вы дали {} верных ответов из {}.'.format(correct, len(questions)))
