a = [i for i in range(11, 80)]

for j in a:
    if j % 3 == 0 and j % 5 == 0:
        print('@@$$')
    elif j % 5 == 0:
        print('@@')
    elif j % 3 == 0:
        print('$$')
    else:
        print(j)
