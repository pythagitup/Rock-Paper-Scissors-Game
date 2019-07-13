from random import choice

def win(a,b):
    if a == b or a[1:] == b[1:]:
        print('It\'s a tie!')
    elif a == 'Rock' or a == 'rock':
        if b == 'Paper':
            print('You lose!')
        else:
            print('You win!')
    elif a == 'Scissors' or a == 'scissors':
        if b == 'Rock':
            print('You lose!')
        else:
            print('You win!')
    else:
        if b == 'Rock':
            print('You win!')
        else:
            print('You lose!')

print('Let\'s play Rock, Paper, Scissors!')

play = input('Enter your choice: ')

choices = ['Rock', 'Paper', 'Scissors']

comp = choice(choices)

print('The computer chooses ' + comp + '.')

win(play, comp)