# zip

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий кортежи поиндексной суммы многочленов.

with open('file1.txt', 'w') as file1:
    file1.write('2*x^2 + 4*x + 8')
with open('file2.txt', 'w') as file2:
    file2.write('3*x^2 + 9*x')

with open('file1.txt','r') as file1:
    m1 = file1.readline()
    list_m1 = m1.split()


with open('file2.txt','r') as file:
    m2 = file.readline()
    list_m2 = m2.split()

list = []
res =zip(list_m1,list_m2)
for e in res:
    list.append(e)
print(list)

with open('result.txt', 'w') as result:
    result.write(str(list))
