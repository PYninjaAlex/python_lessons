players = {'Алекс': 10, 'Роман': 22, 'ГОША': 10, 'brbrtb': 3, 'андрей': 1, 'валера': 3, 'антон': 6, 'фёдор': 0,
           'GRIGIRIY': 0, 'HOMW': 3, 'sdfsdffd': 0, 'dsdf': 0, 'dfdf': 0, 'dfdfd': 0, 'dd': 0, 'cddfdf': 0, 'ваыва': 0}



sorted_list = sorted(players.items(), key=lambda item: item[1], reverse=True)
names = []
nums = []

for z in range(len(sorted_list)):
    names.append(sorted_list[z][0])
    nums.append(sorted_list[z][1])

print('Таблица лидеров')



with open('players.txt', 'w', encoding='utf-8') as outfile:
    outfile.write('Таблица лидеров\n')
    for i in range(len(sorted_list)):
        print(f'{i}. {names[i]} - {nums[i]}')
        outfile.write(f'{i}. {names[i]} - {nums[i]}\n')
