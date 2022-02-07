
# Q1 
a = 80
b = 75
c = 55
print((a+b+c)/3)
#Q1 다른 풀이
a = [80,75,55]
total = 0
for i in a:
    total = total + i
avg = total / len(a)
print(f"평균은 {avg}점 입니다.")


# Q 02
su  =int(input('숫자를 입력하세요:'))
if su % 2 == 0:
    print('짝수입니다.')
else:
    print('홀수입니다.')

# Q 03
주민번호 = '881120-1068234'
yyyymmdd = 주민번호[:6]
나머지 = 주민번호[7:]
print(yyyymmdd)
print(나머지)

# Q 04
pin = '881120-1068234'
if pin[7] == '1':
    print('남자')
else:
    print('여자')
    
a = "a:b:c:d"
b = a.replace(":","#")
print(b)


a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

a = ['life','is','too','short']
result = ' '.join(a)
print(result)


a =(1,2,3)
a = a + (4,)
print(a)

a = dict()
print(a)

## Q10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet =set(a)
b = list(aSet)
print(b)

# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)
