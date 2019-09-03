import math
import numpy as np

#Классы
class Tripple:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def a(self):
        return self._a

    def b(self):
        return self._b

    def c(self):
        return self._c

    
    def __str__ (self):
        return ('(' + str(self.a) + ', ' + str(self.b) + ', ' + str(self.c)+')')


class Vector(Tripple):
    
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def scal(self, v):
        return self.a*v.a + self.b*v.b + self.c*v.c

    def vect(self, v):
        return Vector(self.b*v.c - v.b*self.c, - (self.a*v.c - v.a*self.c), (self.a*v.b - v.a*self.b))

    def vectSum(self, v):
        p = self.vect(v)
        return (p.a+p.b+p.c)

    


class Point(Tripple):
    
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def dist (self, a, b, c, d):
        return int((a*self.a + b*self.b + c*self.c + d)/(a*a + b*b + c*c)**0.5)

    def volume(self, p1, p2, p3):
        v1 = Vector(p1.a - self.a, p1.b - self.b, p1.c - self.c)
        v2 = Vector(p2.a - self.a, p2.b - self.b, p2.c - self.c)
        v3 = Vector(p3.a - self.a, p3.b - self.b, p3.c - self.c)
        return int(1/6*np.abs((v1.vect(v2)).scal(v3)))

    def med(self, p1, p2):
        p = Point((self.a + p1.a + p2.a)//3, (self.b + p1.b + p2.b)//3, (self.c + p1.c + p2.c)//3)
        return p.a + p.b + p.c
        
#Функции

def rint():
    return np.random.randint(-10, 11)

def makeVect():
    return Vector(rint(), rint(), rint())

def makePoint():
    return Point(rint(), rint(), rint())

def makeTriangle():
    flag = True
    while flag:
        a = makePoint()
        b = makePoint()
        c = makePoint()
            
        ab = Vector(b.a - a.a, b.b - a.b, b.c - a.c)
        ac = Vector(c.a - a.a, c.b - a.b, c.c - a.c)
        if ab.vectSum(ac) != 0:
            return a, b, c

def makePyr(a, b, c):
    while True:
        d = makePoint()
        vol = d.volume(a, b, c)
        if vol != 0:
            return d

def makeEq(a, b, c, d):
    s = ''
    if a != 0:
        if a == 1:
            s += 'x '
        elif a == -1:
            s += '-x '
        else:
            s += str(int(a)) + 'x '
    
    if b != 0:
        if a != 0:
            if b > 0:
                s += '+ '
            else:
                s += '- '
        if math.fabs(b) == 1:
            s += 'y '
        else:
            s += str(int(math.fabs(b))) + 'y '

    if c != 0:        
        if (b != 0) | (a != 0):
            if c > 0:
                s += '+ '
            else:
                s += '- '
        if math.fabs(c) == 1:
            s += 'z '
        else:
            s += str(int(math.fabs(c))) + 'z '

    if d != 0:
        if (c != 0) | (b != 0) | (a != 0):
            if d > 0:
                s += '+ '
            else:
                s += '- '
        s += str(int(math.fabs(d)))
    return s

def writeInfo(path, mes):
    try:
        with open(path, 'w') as f:
            f.write(mes)
    except:
        print("Не удалось записать в файл")

    
def appendInfo(path, mes):
    try:
        with open(path, 'a') as f:
            f.write('\n' + mes)
    except:
        print("Не удалось записать в файл")

def checkAnswer(an, cor):
    if (an.isdigit()) | ((an[0] == '-')&(an[1:len(an)].isdigit())):
        if int(an) == cor:
            print("Правильно")
            return False
        else:
            print("Неверно")
            return False
    else:
        print("Ответ - целое число")
        return True

#Задания                     
def n1(v1, v2):
    print('Задание первое:')
    print(f'Найдите скалярное произведение векторов v1 = {str(v1)}, v2 = {str(v2)}:')

    flag = True
    while flag:
        an = input("Ваш ответ: ")
        cor = v1.scal(v2)
        flag = checkAnswer(an, cor)
        
    return (f"1. Найдите скалярное произведение векторов v1 = {str(v1)}, v2 = {str(v2)}. Правильный ответ: {str(cor)}, Ответ пользователя: {an}") 
    
def n2(v1, v2):
    print('Задание второе:')
    print(f'Найдите векторное произведение векторов v1 = {str(v1)}, v2 = {str(v2)} и посчитайте сумму координат вектора:')
    
    flag = True
    while flag:
        an = input("Ваш ответ: ")
        cor = v1.vectSum(v2)
        flag = checkAnswer(an, cor)
        
    return (f"2. Найдите векторное произведение векторов v1 = {str(v1)}, v2 = {str(v2)} и посчитайте сумму координат вектора. Правильный ответ: {str(cor)}, Ответ пользователя: {an}")

def n3(k):
    flag = True
    while flag:
        a = rint()
        b = rint()
        c = rint()
        if (a != 0) | (b != 0) | (c != 0):
            flag = False

    d = rint()
    
    print('Задание третье:')
    print(f"Найдите расстояние от точки K{str(k)} до плоскости {makeEq(a, b, c, d)} = 0 и введите целую часть результата.")
    
    flag = True
    while flag:
        an = input("Ваш ответ: ")
        cor = k.dist(a, b, c, d)
        flag = checkAnswer(an, cor)
        
    return (f"3. Найдите расстояние от точки K{str(k)} до плоскости {makeEq(a, b, c, d)} = 0 и введите целую часть результата.. Правильный ответ: {str(cor)}, Ответ пользователя: {an}")

def n4():
    
    a,b,c = makeTriangle()        
    d = makePyr(a, b, c)
    
    print('Задание четвертое:')
    print(f"Вычислите объем пирамиды ABCD, A{str(a)}, B{str(b)}, C{str(c)}, D{str(d)}:")
    
    flag = True
    while flag:
        an = input("Ваш ответ: ")
        cor = d.volume(a, b, c)
        flag = checkAnswer(an, cor)
        
    return (f"4. Вычислите объем пирамиды ABCD, A{str(a)}, B{str(b)}, C{str(c)}, D{str(d)}. Правильный ответ: {str(cor)}, Ответ пользователя: {an}")

def n5():

    a, b, c = makeTriangle()
    
    print('Задание пятое:')
    print(f'Найдите сумму целых частей координат точки пересечения треугольника ABC, A{str(a)}, B{str(b)}, C{str(c)}:')

    flag = True
    while flag:
        an = input("Ваш ответ: ")
        cor = a.med(b, c)
        flag = checkAnswer(an, cor)
        
    return (f"5. Найдите сумму целых частей координат точки пересечения треугольника ABC, A{str(a)}, B{str(b)}, C{str(c)}. Правильный ответ: {str(cor)}, Ответ пользователя: {an}") 


def getfio():
    flag = True
    while flag:
        print("Введите ФИО, чтобы пройти тестирование")
        fio = input()
        fioSpl = fio.split()
        if len(fioSpl) == 3:
            fam = fioSpl[0]
            if fio.replace(' ','').isalpha():
                flag = False
                
            else:
                print("Неверный ввод (ФИО состоит только из букв)")
        else:
            print("Неверный ввод (ФИО состоит из трех слов)")
    return fioSpl


#Программа

fioSpl = getfio()
path = 'test_' + fioSpl[0] + fioSpl[1][0].upper() + fioSpl[2][0].upper() + '.txt'

v1 = makeVect()
v2 = makeVect()
k = makePoint()

writeInfo(path, (n1(v1, v2)))
appendInfo(path, (n2(v1, v2)))
appendInfo(path, (n3(k)))
appendInfo(path, (n4()))
appendInfo(path, (n5()))










