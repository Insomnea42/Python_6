#filter

n = [1, 6, 2, 4, 3, 5, 4, 10]
sum = 0
g =[]
g = list(filter(lambda x: not x%2,n))
print(g)
for i in g:
    sum +=i
print(f'Список: {n}')
print(f'Сумма элементов нечетных: {sum}')