from multiprocessing import Condition
import secrets


secrets_number = 4
guess_count = 0
guess_limit = 3
while guess_count < guess_limit :
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secrets_number:
        print('You won!')
        break
else:
    print('Sorry, you failed!')