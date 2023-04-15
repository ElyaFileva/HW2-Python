from random import randint
count_of_coin = int(input('Введите количество монет N: '))
coin0 = 0
coin1 = 0
for i in range(count_of_coin):
    coin = int(randint(0, 1))
    print(coin)
    if coin == 0:
        coin0 += 1
    else:
        coin1 += 1
print(f'Количество монет решкой вверх: {coin0}, гербом вверх: {coin1}')
if coin0 >= coin1:
    print(f'Минимальное количество монет, которые нужно перевернуть: {coin1}')
else:
    print(f'Минимальное количество монет, которые нужно перевернуть: {coin0}')
