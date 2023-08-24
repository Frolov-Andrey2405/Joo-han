import random
import sys

JAPANESE_NUMBERS = {
    1: 'ICHI', 2: 'NI', 3: 'SAN',
    4: 'SHI', 5: 'GO', 6: 'ROKU'
}


def get_valid_bet(purse):
    while True:
        pot = input(f'You have {purse} mon. How much do you bet? (or QUIT) > ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            return int(pot)


def main():
    print('''
    In this traditional Japanese dice game, two dice are rolled in a bamboo
    cup by the dealer sitting on the floor. The player must guess if the
    dice total to an even (cho) or odd (han) number.
    ''')

    purse = 5000
    while True:  # Main game loop.
        pot = get_valid_bet(purse)

        # Roll the dice.
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print('The dealer swirls the cup and you hear the rattle of dice.')
        print('The dealer slams the cup on the floor, still covering the')
        print('dice and asks for your bet.\n')
        print('    CHO (even) or HAN (odd)?')

        # Let the player bet cho or han.
        bet = input('> ').strip().upper()
        while bet not in ['CHO', 'HAN']:
            print('Please enter either "CHO" or "HAN".')
            bet = input('> ').strip().upper()

        # Reveal the dice results.
        print('The dealer lifts the cup to reveal:')
        print(f'  {JAPANESE_NUMBERS[dice1]} - {JAPANESE_NUMBERS[dice2]}')
        print(f'    {dice1} - {dice2}')

        # Determine if the player won.
        rollIsEven = (dice1 + dice2) % 2 == 0
        correctBet = 'CHO' if rollIsEven else 'HAN'
        playerWon = bet == correctBet

        # Display the bet results.
        if playerWon:
            print(f'You won! You take {pot} mon.')
            house_fee = pot // 10
            purse += pot - house_fee
            print(f'The house collects a {house_fee} mon fee.')
        else:
            purse -= pot
            print('You lost!')

        # Check if the player has run out of money.
        if purse == 0:
            print('You have run out of money!')
            print('Thanks for playing!')
            sys.exit()


if __name__ == "__main__":
    main()
