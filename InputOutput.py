def task_one():
    '''
    УСЛОВИЕ: Напишите программу, которая считывает три числа и выводит их сумму. Каждое число записано в отдельной строке.
    :return:
    '''
    print('The first task:')
    a = int(input('First number: '))
    b = int(input('Second number: '))
    c = int(input('Third number: '))
    print(int(a + b + c))


def task_two():
    '''
    УСЛОВИЕ: Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь. Каждое число записано в отдельной строке.
    :return:
    '''
    print('The second task:')
    a = int(input('Enter lenght of the first cathetus: '))
    b = int(input('Enter lenght of the second cathetus: '))
    print('Square of triangle = ' + str((a * b) / 2))


def task_three():
    '''
    УСЛОВИЕ: n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
    Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?
    Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).
    :return:
    '''
    print('The third task:')
    n = int(input('Enter number of children: '))
    k = int(input('Enter number of apples: '))
    print('Each child will get apples: ' + str(k // n))
    print('Apples left: ' + str(k % n))


def task_four():
    '''
    Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы
     в этот момент. Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
     Учтите, что число n может быть больше, чем количество минут в сутках.
    :return:
    '''
    print('The fourth task:')
    n = int(input('How many minutes have passed since the start of the day?: '))
    print('Time is: ' + str(n // 60) + ':' + str(n % 60))  # Можно было бы использовать соответствующий модуль, но смысл данного раздела в другом, как я понимаю


def task_five():
    '''
    УСЛОВИЕ: Напишите программу, которая приветствует пользователя, выводя слово Hello,
    введенное имя и знаки препинания по образцу: Hello, Harry!
    :return:
    '''
    print('The fifth task:')
    name = input('What\'s your name?: ')
    print(f'Hello, {name}!')


def task_six():
    '''
    УСЛОВИЕ: Напишите программу, которая считывает целое число и выводит текст,
    аналогичный приведенному в примере (пробелы важны!). "The next number for the number 1534 is 1535.
    The previous number for the number 1534 is 1533."
    :return:
    '''
    print('The sixth task:')
    a = int(input('Enter the number: '))
    print(f'The next number for the number {a} is {a + 1}')
    print(f'The previous number for the number {a} is {a - 1}')


def task_seven():
    '''
    УСЛОВИЕ: В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят
    в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты. За каждой
    партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько
    всего нужно закупить парт чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа:
    количество учащихся в каждом из трех классов.
    :return:
    '''
    print('The seventh task:')
    a = int(input('Enter number of students for the first class: '))
    b = int(input('Enter number of students for the second class: '))
    c = int(input('Enter number of students for the third class: '))

    amount = (a // 2 + a % 2) + (b // 2 + b % 2) + (c // 2 + c % 2)

    print(f'Total desks: {amount}')


if __name__ == '__main__':
    task_one()
    task_two()
    task_three()
    task_four()
    task_five()
    task_six()
    task_seven()
