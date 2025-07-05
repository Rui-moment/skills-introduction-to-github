import random, sys

wins = 0
losses = 0
ties = 0

while True:
    print(str(wins) + ' wins, ' + str(losses) + ' losses, ' + str(ties) + ' ties')
    print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
    while True:
        player_move = input()
        if player_move == 'q':
            print('Thanks for playing!')
            sys.exit()
        if player_move not in ('r', 'p', 's'):
            print('Please enter one of r, p, s, or q.')
            continue
        break

    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_number == 3:
        computer_move = 's'
        print('SCISSORS')

    if player_move == computer_move:
        print('It is a tie')
        ties += 1
    elif player_move == 'r' and computer_move == 's':
        print('You win! ROCK beats SCISSORS')
        wins += 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win! PAPER beats ROCK')
        wins += 1
    elif player_move == 's' and computer_move == 'p':
        print('You win! SCISSORS beats PAPER')
        wins += 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose! PAPER beats ROCK')
        losses += 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose! SCISSORS beats PAPER')
        losses += 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose! ROCK beats SCISSORS')
        losses += 1
