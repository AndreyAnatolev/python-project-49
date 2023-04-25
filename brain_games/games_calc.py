
from random import randint
from random import choice

def calc(user_name):
    print('What is the result of the expression?')
    count = 0
    for i in range(3):
        a = randint(1, 99)
        b = randint(1, 99)
        list1 = ['+', '-', '*']
        operation = choice(list1)
        print('Question: ', a, operation, b)
        answer_user = ''
        while answer_user == '':
            print('Your answer: ', end='')
            answer_user = input()
            if operation == '+':
                answer_game = a + b
            elif operation == '-':
                answer_game = a - b
e        if answer_user == str(answer_game):
            count += 1
            print('Correct!')
            if count == 3:
                print(f'Congratulations, {user_name}!')
        else:
            print(f"'{answer_user}' is wrong answer ;(."
                  f"Correct answer was '{answer_game}'. "
                  f"Let's try again, {user_name}!")
            break
