k = int(input('Ввод числа от 3 до 20:  '))
if k <= 20 and k >=3:
    string = ''
    for i in range(1, k):
        for j in range(i+1, k):
            if k % (i+j)==0:
                string = string + str(i) + str(j)
    print(k, ':', string)
else:
    print('Ввод другого числа')
