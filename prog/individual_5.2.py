a = float(input('Введите положительное число для \"a\": '))
b = float(input('Введите положительное число для \"b\": '))
M = input('Введите для точки \"M\" координаты X,Y: ').split(',')
X = float(M[0])
Y = float(M[1])
tan = b/a
if a>0 and b>0 and (Y/X < b/a):
    print('True')
else:
    print('False')
