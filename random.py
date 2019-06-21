import random

num1 = 1
num2 = 100
game = False
ans = 0
while game == False:
    
    number = (num1+num2) // 2
    print (number)
    ans = input("Угадал - 'верно', моё число больше - '>' ,моё число меньше - '<': ")

    if ans == '<':
        num2 = number
        
    if ans == '>':
        num1 = number

    if ans == 'верно':
        print('Ура!')
        game = True
