from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('''Answer "yes" if the number is even, otherwise answer "no".''')
    count = 0
    for i in range(3):
        n = randint(1, 99)
        print('Question:', n)
        answer_user = ''
        while answer_user == '':
            print('Your answer: ', end='')
            answer_user = input()
        answer_random = 'no'
        if n % 2 == 0:
            answer_random = 'yes'
        if answer_random == answer_user:
            count += 1
            print('Correct!')
            if count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{answer_user}' is wrong answer ;(."
                  f"Correct answer was '{answer_random}'. "
                  f"Let's try again, {name}!")
            break


if __name__ == '__main__':
    main()
