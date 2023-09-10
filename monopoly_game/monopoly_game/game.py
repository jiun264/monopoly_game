from monopoly_game import Monopoly
import matplotlib.pyplot as plt
# Instantiate Monopoly game


win = [0 for i in range(4)]
end_round = [0 for i in range(3000)]
win_place = {}
lose_place = {}
jail_fee = 100
acc = [0]
money = 0
d = []
it = 100
# Play the game
for i in range(it):
    game = Monopoly(jail_fee)
    game.play_game()
    x = game.get_winner()
    money += x[3]
    if x[-2] == True:
        break
    print("x:", x)
    if x[-1].name in win_place.keys():
        win_place[x[-1].name] += 1
    else:
        win_place[x[-1].name] = 1
    for j in range(2):
        if x[1][j].name in lose_place.keys():
            lose_place[x[1][j].name] += 1
        else:
            lose_place[x[1][j].name] = 1
    win[int(x[0].name[-1])] += 1
    end_round[x[2]] += 1
    if i%1000 == 0:
        if '監獄' in lose_place.keys():
            acc.append(lose_place['監獄'] - acc[-1])
            d.append(lose_place['監獄'])
        else:
            acc.append(0)
            d.append(0)
        if lose_place['監獄'] > i/2:
            jail_fee -= 10
print("Winner's money average: ", money/it)
print(win[1], win[2], win[3])
win_place = dict(sorted(win_place.items(), key=lambda item: item[1]))
for i in win_place.keys():
    print(i,win_place[i])
print("-----------------")
lose_place = dict(sorted(lose_place.items(), key=lambda item: item[1]))
for i in lose_place.keys():
    print(i, lose_place[i])
plt.hist(end_round)
plt.show()
