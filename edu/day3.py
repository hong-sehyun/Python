#collection data types
#list
'''
#리스트 컴프리헨션
even_num = [num for num in range(1,11) if num%2==0]
print(even_num)

origin_list = [1,2,3]
new_list = [num +1 for num in origin_list]
print(new_list)

origin_list2 = [[1,2], [3,4], [5,6]]
new_list2 = [num for sublist in origin_list2 for num in sublist]
print(new_list2)

#리스트 인덱싱
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(matrix[0])
print(matrix[0][1])

#리스트 슬라이싱
my_list = [1,2,3,4,5]
print(my_list[1:4])
#끝에서 부터 추출
print(my_list[-3:])

#리스트 합치기
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2

#extend() 이용


#리스트 수정 추가 제거

#내장 함수 이용해서 리스트 다루기
#sorted(), sort()
#sorted는 새로운 리스트 반환(원본 리스트 변경x), sort는 원본 리스트가 변경
nums = [3,4,1,5,2]
sorted_nums = sorted(nums)
print(sorted_nums)
#reversed()는 새로운 리스트 반환(원본 리스트 변경x), reverse()는 원본 리스트가 변경

#연습문제
names = ['hong', 'kim', 'lee']
names.insert(0, 'choi')
print(names)
names.insert(2, 'park')
print(names)
names.append('jung')
print(names)

#연습문제1
nums1 = [num for num in range(0, 50)]
print(nums1)
nums2 = [num*num for num in range(1, 51)]
print(nums2)

#연습문제2
L, M, N = [1,2,3], [4,5,6], []
for i in range(len(L)):
    N.append(L[i]+M[i])
print(N)

#연습문제3
num_list = input("5개 숫자 입력(구분자 : 띄어쓰기):").split()
result = '+'.join(num_list)
print(result)

#tuple

#dictionary
#fruits = {'apple': 3, 'banana': 2, 'orange': 1}
#연습문제
'''
days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June':30}

'''
month = input("월 입력 : ")
print(days[month.title()])

days_key = days.keys()
print(sorted(days_key))

for mon in days:
    if days[mon] == 31:
        print(mon, end =  ' ')
        
days_item = days.items()
r_days = [(day, month) for (month, day) in days_item]
r_days.sort()
days2 = [(month, day) for (day, month) in r_days]
print(days2)


month2 = input("월 3자리 입력 : ")
for mon in days:
    if mon[0:3] == month2.title():
        print(days[mon])


d=[{'name':'Todd', 'phone':'555-1414','email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618','email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3141', 'email':''},{'name':'LJ', 'phone':'555-2718',
'email':'lj@mail.net'}]

for people in d:
    if people['phone'][7] == '8':
        print(people['name'])
        
for people in d:
    if people['email']=='':
        print(people['name'])

s_name = input("찾을 이름을 입력하세요 : ")
flag = 1
for people in d:
    if people['name']==s_name:
        print(people['phone'], people['email'])
        flag = 0
    
if flag == 1 :
    print("이름이 없습니다")

#set
#remove 와 discard의 차이
import random
pick = set()
while len(pick)<6:
    n = random.randint(1,46)
    pick.add(n)
    
print(sorted(pick))


score = {"Alice": [85, 90, 95],
"Bob": [75, 80, 85],
"Charlie": [95, 95, 95]}

for name, grade in score.items():
    avg = sum(grade)/len(grade)
    print(f"{name} : {avg}")
    
nums = set([1,2,2,3,3,3,4,4,5])
print(sum(nums))


text = "Hello,World"
temp_dict = {}
for char in text:
    if char not in temp_dict :
        temp_dict[char] = 1
    else :
        temp_dict[char] += 1
print(temp_dict)

set1 = set([1,2,3,4,5])
set2 = set([2,4,6,8,10])
print(list(set1 & set2))


def sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total;
print(sum(50))

#지역변수와 전역변수
x = 1 #전역변수 
def my_func():
    y = 2 #지역변수
    print('y:', y)
    print('x:', x)
my_func()
#print('x:', x)

lambda_add = lambda a, b: a + b
result = lambda_add(3,4)
print(result)


def get_operator(operator):
    if operator == '+':
        return lambda a, b : a + b
    elif operator == '-':
        return lambda a, b : a - b
    elif operator == '*':
        return lambda a, b : a * b
    elif operator == '/':
        return lambda a, b : a / b
add_func = get_operator('+')
result1 = add_func(3,4)

multi_func = get_operator('*')
result2 = multi_func(3,4)
print(result1)
print(result2)
'''

def box(n, m):
    for i in range(n):
        print('*', end='')
        for j in range(m):
            print('\n')
box(2, 4)
