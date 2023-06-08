'''
def outer_func(x):
    def inner_func(y):
        return x+y
    return inner_func

result = outer_func(10)
print(result(20)) #20은 y에 들어감. 결과: 30

def calsulator():
    def add(a, b):
        return a + b
    
'''
#내부함수는 코드의 재사용성을 높일 수 있음
'''

def power(n):
    def inner(x):
        return x**n
    return inner

square = power(2)
cube = power(3)

print(square(3))
print(cube(3))

#*args

#**kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
print_info(name = 'Alice', age = 25, country = 'usa')

#함수 내 변수 참조 순서


#내장함수
s = int('1010', base=10)
b = 1
print(s+b)

#zip

names = ['A', 'b', 'c']
ages = [24, 32, 28]
for name, age in zip(names, ages):
    #print(zip(names, ages))
    print(name, age)
print(dict(zip(names, ages)))


#연습문제
#1
def findchar(char) :
    enumerate



def cal():
    def sum(a, b):
        return a+b
    def sub(a, b):
        return a-b
    def mul(a, b):
        return a*b
    def div(a, b):
        return a/b
    return sum, sub, mul, div
sum, sub, mul, div = cal()
table = {'1' : sum, '2' : sub, '3': mul, '4' : div}
a = int(input("a입력:"))
b = int(input("b입력:"))
get = input("숫자를 입력하세요")


def query_parse(txt):
    items = txt.split('&')
    temp = []
    for item in items :
        temp.append(item.split('='))
    return dict(temp)
txt = 'led=on&motor=off&switch=off'
print(query_parse(txt))

'''