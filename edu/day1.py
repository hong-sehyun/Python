a = [1, 2, 3, 4, 5]
b = "Hello, World!"
print(3 in a)
print(6 in a)
print("o" in b)
print("k" not in b)

x = 10
y = 5
z = x+ y
print(x,y,z)
print(10+20)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits)

print(fruits[0])

"""
person = {"name": "John", "age": 25, "city": "New York"}
print(person)

print(person["name"])
"""

"""
name = "John"
age = 30
height = 175.5
print("My name is {}, I'm {} years old, and my height id {:.1f}.".format(name, age, height))

#f-string
name = "John"
age = 30
height = 175.5
print(f"My name is {name}, I'm {age} years old, and my height id {height:.1f}.")

#활용
w = 12345
print(f"The value of w is {w:0>10d}.")
print(f"The value of w is {w:*>10d}.")
print(f"The value of w is {w: >10d}.")
print(f"The value of w is {w:10d}.")

z = 12.345
print(f"The value of z is {z:10.2f}.")

#가운데 정렬
text = "Hello, world!"
print(f"\"{text:^20}\"")

#문제
name = "Tom"
age = 20
print(f"My name is {name} and I am {age} years old.")

"""

#input
"""
name = input("What is your name?")
print(f"Hello, {name}!")


#예제

cnt = int(input("사과의 개수를 입력하세요:"))
price = int(input("사과의 가격을 입력하세요:"))
tax = int(input("부과세율을  입력하세요:"))

p2 = cnt*price
t2 = p2*tax//100
total = t2 + p2

print(f"{total} 원")


#추가문제

num = int(input("초 입력:"))
minute = num//60
second = num%60
print(f"{minute}분{second}초")



time = int(input("분 입력:"))
minute = time%60
hour = (time//60)%24
day = time//1440
print(f"{day}일{hour}시간{minute}분")


"""

n = 5000000
i = 0.05
n += n*i
n += n*i
n += n*i
n += n*i
n += n*i

print(f"금액: {int(n)}원")


'''
n1 = 100
sum = n1*(n1+1)//2
print(sum)
'''
'''
gn = int(input("포도 알의 개수 :"))
sn = int(input("딸기의 개수 :"))
g = 75*gn
s = 113.5*sn

print(f"총{g+s}")

'''

'''
ko = int(input("국어 성적 :"))*0.4
en = int(input("영어 성적 :"))*0.4
m = int(input("수학 성적 :"))*0.2

avg = ko + en + m

if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
elif avg < 60:
    grade = "F"
   
#grade = "A" if avg >= 90 else("B" if avg >= 80 else("C" if avg >= 70 else( "D" if avg >=60 else("F" if avg < 60)
print(f"평균 {avg:.2f}")
print(f"학점 {grade}")
'''
'''
cm = int(input("cm :"))
if cm < 0:
    result = "잘못 입력 하였습니다"
else:
    inch = cm*2.54
    print(inch)
    

n = int(input("n:"))

if n < 40:
    grade = "1학년 입니다"
elif n>=40 and n<80:
    grade = "2학년 입니다"
elif n>= 80:
    grade = "졸업반 입니다"
print(grade)


#내가 한 것
time = int(input("1~12 숫자:"))
pa = input("pm or am:")
long = int(input("시간이 얼마나 흘렀나?"))

if pa == "pm" :
    if (time + long) > 12:
        newpa = "am"
        time = time + long -12
        print(f"{time}{newpa}")
    elif (time + long) == 12:
        newpa = "am"
        time = time + long
        print(f"{time}{newpa}")
    else :
        time = time + long
        print(f"{time}{pa}")
elif pa == "am" :
    if (time + long) > 12:
        newpa = "pm"
        time = time + long -12
        print(f"{time}{newpa}")
    elif (time + long) == 12:
        newpa = "pm"
        time = time + long
        print(f"{time}{newpa}")
    else :
        time = time + long
        print(f"{time}{pa}")
    '''
#교수님꺼
time = int(input("현재 시간(1~12):"))
apm = input("pm or am:")
over_time = int(input("추가 시간:"))

new_time = (time + over_time)%12

if new_time == 0:
    new_time = 12
if (time + over_time) // 12 % 2 == 1:
    if apm == 'am':
        apm = 'pm'
    else :
        apm = 'am'
print(f"최종 시간: {new_time} {apm}")
    
