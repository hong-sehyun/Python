'''
i = 1;
while i <=10:
    print (i)
    i += 1
   
colors = ("red", "green", "blue")

for color in colors :
    print(color)
    
  
for i in range(1, 11):
    print(i)
    
#문자로 별모양 그리기
    
    for i in range(1, 6):
        for j in range (1, i+1):
            print("*"
            
 #1부터 n까지의 자연수 중에서 3의 배수와 5의 배수의 합 구하기
n = int(input("n 입력 :"))
sum = 0
for i in range(1, n+1):
    if i%3 == 0 or i%5 == 0:
        sum += i      
print(sum)  

#정수 5개 입력받아서 최댓값 최소값 구하기
max = 0;
min = 100;
for i in range(5):    
    n = int(input("n 입력 :"))

    if n > max :
        max = n
    if n < min :
        min = n
print(f"min {min} max {max}")


sum = 0
while sum < 100 :
    n = int(input("n 입력 :"))
    sum += n

print(sum)


sum = 1
n = int(input("n 입력 :"))
if n ==1 or n==2:
    sum = 1
#    print(1)
else :
    a, b=1, 1
    i = 3
    while i <=n:
        sum = a+b
        a=b
        b = sum
        i+= 1

print(sum)

#주사위 게임
import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
if dice1 + dice2 == 7:
    print(f"{dice1}+{dice2}={dice1 + dice2}이겼습니다")
else :
    print(f"{dice1}+{dice2}={dice1 + dice2}졌습니다")


#계산기 프로그램
while True:
    n1 = input("n1 입력 exit 입력시 종료:")
    
    if n1 == "exit":
        break
    
    n2 = int(input("n2 입력:"))
    x = input("연산자:")
    if n1 != exit:
        
        n1 = int(n1)
        
        if x == "+":
            print(f"{n1}{x}{n2}={n1 + n2}")
        if x == "-":
            print(f"{n1}{x}{n2}={n1 - n2}")
        if x == "*":
            print(f"{n1}{x}{n2}={n1 * n2}")
        if x == "/":
            print(f"{n1}{x}{n2}={n1 // n2}")
    
        if x == "+":
            print(f"{n1}{x}{n2}={n1 + n2}")
        if x == "-":
            print(f"{n1}{x}{n2}={n1 - n2}")
        if x == "*":
            print(f"{n1}{x}{n2}={n1 * n2}")
        if x == "/":
            print(f"{n1}{x}{n2}={n1 // n2}")



#제어문 예제
import random
n = random.randint(1,4)
x = int(input("숫자 입력:"))
for i in range(4):
    x = int(input("숫자 입력:"))
    if n == x :        
        break
    else : continue
    

#연습문제
from random import randint
money = 50

while True:
    
    if money > 0 or money < 100 :
        coin = randint(1,2)
        i = int(input("앞면(1) 뒷면(2) 입력:"))
        if i == coin:
            money += 9
            
        else :
            money -= 10
        
    if money < 0 or money > 100:
        break
    print(money)
    
    
#연습문제-최대공약수
a = int(input("숫자1 입력:"))
b = int(input("숫자2 입력(숫자1 보다 큰 수):"))
m = 0
i=0
while True:
    i+=1
    if a%i == 0 and b%i == 0:
        m = i
        
    if i > a :
        break
print(m)

#연습문제 1
m = int(input("숫자 입력:"))
yak = 100
i=m
while True:
    if m%i == 0:
        yak = i
        print(yak, end=" ")
    i-=1
    if i < 1 :
        break
    else :
        continue


#연습문제 2

while True :
    score = int(input("점수 입력:"))
        
    if score >= 90:
        grade = "A"
        print(grade)
    elif score >= 80:
        grade = "B"
        print(grade)
    elif score >= 60:
        grade = "C"
        print(grade)
    elif score >= 40:
        grade = "D"
        print(grade)
    elif score <= 39:
        grade = "F"
        print(grade)
    if score < 0:
        break

#문자열 슬라이싱
string = "hello world"
substring = string[6:11]
print(substring)



s = "hello world!"

#1
print(len(s))
#2
for i in range(10):
    print(s)
#3
print(s[0])
#4
print(s[0:3])
#7
if len(s) :

#연습문제
w = input("문자 입력:")

1번 방법
a = w.find('a')

if a != -1:
    print(w[:a+1])
    print(w[a+1:])
else:
    print(w)

2번 방법
print(w.replace('a','a\n'))

total = 0
for num in range(1,1001):
    sum = 0
    
    for i in str(num) :
        sum += int(i)
    total += sum
print(total)
    '''


