with open('poem.txt', 'r', encoding='utf-8') as f:
    s = f.read()
a = s.split('\n')
c = s.count('\n')
for i in range(c):
    p = input()
    if p == '':
        print(a[i])
    else:
        print('Нажмите enter')