lst=[
    ['nastya','1234',[12,10,9,7,5,4]],
    ['anna','1111',[8,6,10,3,12,9]],
    ['anton','2222',[12,11,4,2,7,9]],
    ['ivan','3333',[6,5,3,4,8,10]]
]

login= input('Введіть логін:')
pas=input('Введіть пароль:')

a=0
b=0
ok=False
i=0

while i<4:
    item=lst[i]

    if login == item[0] and pas == item[1]:
        ok=True
        gr=item[2]
        break

    i=i+1
if ok ==True:
    print('Вхід успішний!')
    print('Ваші оцінки:')

    for item in gr:

        if item < 1 or item >12:
            continue

        print(item)

        if item >= 5 and item <=12:
            a=a+1

        elif item >= 1 and item <= 4:
            b=b+1
    print('Кількість оцінок від 5 до 12:', a)
    print('Кількість оцінок від 1 до 4:', b)

    if a>0:
        print('Задовільні оцінки є')

    if b !=0:
        print('Незадовільні оцінки є')

    if login in['nastya','anna','anton','ivan']:
        print('Користувач знайдений')

    if not b==0:
        print('Є оцінки від 1 до 4')

    if ok is True:
        print('True')

else:
    print('False')
    print('Неправильний логін або пароль')
