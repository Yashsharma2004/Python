import random
num=random.randint(1,100)
attempts = 10
while attempts:
    user_num=int(input('guess a number between 1 to 100:'))
    attempts -= 1
    print(f'number of attempts left{attempts}')
    if user_num < num:
        print('too small')
    elif user_num > num :
        print('too large')
    else:
        print('You won!')
        break
else:
    print(f'You failed to guess the number{num}')