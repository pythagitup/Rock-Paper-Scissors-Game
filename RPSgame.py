from random import choice

rock = {'rock', 'Rock', 'r', 'R', 'ROCK'}
paper = {'paper', 'Paper', 'p', 'P', 'PAPER'}
scissors = {'scissors', 'Scissors', 's', 'S', 'SCISSORS'}

def whowins(a,b):
    if (a in rock and b in rock) or (a in paper and b in paper) or (a in scissors and b in scissors):
        return 0
    elif a in rock:
        if b in paper:
            return -1
        else:
            return 1
    elif a in scissors:
        if b in rock:
            return -1
        else:
            return 1
    else:
        if b in rock:
            return 1
        else:
            return -1

play = True

win = 0
lose = 0
tie = 0

while play:
    print('Let\'s play Rock, Paper, Scissors!')
    userplay = input('Enter your choice: ')
    choices = ['Rock', 'Paper', 'Scissors']
    comp = choice(choices)
    print('The computer chooses ' + comp + '.')
    if whowins(userplay, comp) == 1:
        win += 1
        print('You win!')
    elif whowins(userplay,comp) == -1:
        lose += 1
        print('You lose!')
    elif whowins(userplay,comp) == 0:
        tie += 1
        print('It\'s a tie!')
    print('Wins: ' + str(win) + ' Losses: ' + str(lose) + ' Ties: ' + str(tie))
    again = input('Would you like to play again? ')
    if again not in {'yes', 'Yes', 'y', 'Y'}:
        play = False