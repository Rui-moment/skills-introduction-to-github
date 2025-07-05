import random
10
secret_number = random.randint(1, 20)
print('１から２０までの数を当ててください')

for guesses_taken in range(1, 7):
    print('あなたの予想は？')
    guess = int(input())

    if guess < secret_number:
        print('あなたの予想は小さすぎます。')
    elif guess > secret_number:
        print('あなたの予想は大きすぎます。')
    else:
        break

if guess ==secret_number:
    print('おめでとう！あなたは' + str(guesses_taken) + '回目で正解しました！')
else:
    print('残念！正解は' + str(secret_number) + 'でした。')