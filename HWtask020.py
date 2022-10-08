# Даны два файла, в каждом из которых находится 
# запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.

from gettext import find

## определяем коэффициент 
def coeff(string0, degree):
    if degree == 0: 
        x = string0.find(' =')
    elif degree == 1: 
        x = string0.find('x ')
    else:
        x = string0.find('x^'+str(degree))
    print(max_degree, degree, x, string0[x-1])
    if x == -1: return 0
    res = ''
    while x>=0 and string0[x-1] != ' ':
        res = string0[x-1] + res
        x -= 1
    ##print(max_degree, degree, x, string0[x-1], res)
    return int(res)

data1 = open('D:\SASLearn\HW(python)\HWtask020\data1.txt', 'r')
data2 = open('D:\SASLearn\HW(python)\HWtask020\data2.txt', 'r')
data3 = open('D:\SASLearn\HW(python)\HWtask020\data3.txt', 'w')
string1 = data1.readline()
string2 = data2.readline()
string3 = ''

## определяем наибольшую степень
max1 = int(string1[string1.find('x')+2])
max2 = int(string2[string2.find('x')+2])
max_degree = max(max1, max2)

## формируем строку с суммой и выводим в файл
for i in range(max_degree, 1, -1):
    string3 += str(coeff(string1, i) + coeff(string2, i))+'x^'+str(i)+' + ' 
string3 += str(coeff(string1, 1) + coeff(string2, 1))+'x'+' + '
string3 += str(coeff(string1, 0) + coeff(string2, 0))+' = 0'
data3.write(string3)
data1.close()
data2.close()
data3.close()