# 나이 구하기
def solution1(age):
  if 0 < age <= 120:
    age = 2022 - (age - 1)
  answer = age
  return answer


# n이하 짝수의 합
def solution2(n):
  # answer = []
  # for i in range(n+1):
  #   if i % 2 == 0:
  #     answer.append(i)
  answer = [i for i in range(n+1) if i % 2 == 0]
  answer = sum(answer)
    
  return answer


# 배열의 평균값
def solution(numbers):
  answer = sum(numbers) / len(numbers)
  return answer


# 옷가게 할인
def solution(price):

  sale = 0
  
  if price >= 500000:
    sale = price * 0.2
    print('price: ', price, 'sale: ', sale)
  elif price >= 300000:
    sale = price * 0.1
    print('price: ', price, 'sale: ', sale)
  elif price >= 100000:
    sale = price * 0.05
    print('price: ', price, 'sale: ', sale)

  answer = int(price - sale)
  
  return answer


# 아아메
def solution(money):

  coffee = 5500
  budget = 0

  num = int(money / coffee)
  budget = int(money - (num * coffee))

  answer = [num, budget]

  return answer


# 배열 뒤집기
def solution(num_list):

  num_list.reverse()
  
  answer = num_list
  return answer


# 피자나눠먹기1
import math
def solution(n):

  answer = 0
  
  if n % 7 != 0:
    answer = math.ceil(n / 7)
  elif n % 7 == 0:
    answer = int(n / 7)

  return answer


# 피자노나먹기2
import math
def solution(n):

  answer = 0

  # 인원이 6조각으로 나누어 떨어지는 경우, 해당 몫을 피자 판 수로 할당
  if n % 6 == 0:
    answer = int(n / 6)
  # 인원이 6조각으로 나누어 떨어지지 않는 경우, 인원과 6의 최소공배수를 6으로 나누어 할당
  if n % 6 != 0:
    answer = int(lcm(n, 6) / 6)

  return answer

def lcm(a, b):
  return abs(a * b) // math.gcd(a, b)
  

# 피자노나먹기3
def solution(slice, n):
  answer = 0

  if n <= slice:  # 인원 <= 조각
      answer = 1
  else:  # 인원 > 조각
      if (n / slice) % 1 == 0:  # 나누어 떨어짐
          answer = int(n / slice)
      else:  # 안 나눠짐(한 판 추가)
          answer = int(n / slice) + 1

  return answer
# print(solution(4, 12))


# 양꼬치
import math
def solution(n, k):

  total = ( 12000 * n ) + ( 2000 * k )
  num = 0

  if n >= 10:
    num = math.floor( n / 10 )
    answer = total - ( 2000 * num )
    print('10이상', num, total)
  elif n < 10:
    answer = total
    print('10미만', total)
  
    return answer
# print(solution(64, 6))


# 키큰사람
def solution(array, height):
  answer = 0
  for i in array:
    if i > height:
      answer += 1
  return answer
# print(solution([149, 180, 192, 170], 167))
  

# 중복숫자개수
def solution(array, n):

  answer = sum(1 for value in array if value == n)
  
  return answer
# print(solution([1, 2, 2, 2, 3, 4], 2))


# 가위바위보
def solution(rsp):
  answer = ''
  # 가위(2), 바위(0), 보(5)
  win = {'2':'0', '0':'5', '5':'2'}

  for char in rsp:
    answer += win[char]
  
  return answer
# print(solution('20'))


# 개미군단
def solution(hp):
  answer = 0

  # 5로 나눈 몫 더하고 나머지 값 저장
  answer += hp // 5
  hp %= 5

  # 3으로 나눈 몫 더하고 나머지 값 저장
  answer += hp // 3
  hp %= 3

  # 나머지 값 더함
  answer += hp
  
  return answer
# print(solution(999))


# 특정 문자 제거
def solution(my_string, letter):
  answer = ''

  if letter in my_string:
    for char in my_string:
      if char != letter:
        answer += char
  else:
    answer = my_string
  
  return answer
# print(solution("B", "b"))


# 문자열뒤집기(검색)
def solution(my_string):
  answer = my_string[::-1]
  return answer


# 직각삼각형
n = 3

# for i in range(n):
  # print((i + 1) * "*")


# 짝수홀수개수
def solution(num_list):

  even = 0
  odd = 0

  even = sum(1 for i in num_list if i % 2 == 0)
  odd = sum(1 for i in num_list if i % 2 != 0)

  answer = [even, odd]

  return answer


# 문자반복출력
def solution(my_string, n):

  answer = ''
  
  for char in my_string:
    answer += char * n
  
  return answer


# 배열 자르기
def solution(numbers, num1, num2):
  answer = numbers[num1:num2+1]
  
  return answer


# 외계행성나이
def solution(age):

  age_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j'}
  answer = ''
  for char in str(age):
    answer += age_dict[int(char)]
  
  return answer


# 진료순서정하기
def solution(emergency):

  sorted_array = sorted(emergency, reverse=True)
  answer = [sorted_array.index(i) + 1 for i in emergency]
  
  return answer


# 순서쌍의 개수
def solution(n):
  answer = 0

  # 약수 전부 구하기??
  for i in range(1, n+1):
    if n % i == 0:
      answer += 1

  return answer


# 모스부호1
def solution(letter):

  answer = ''
  morse = { 
      '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
      '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
      '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
      '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
      '-.--':'y','--..':'z'
  }

  words = letter.split(' ')  # 공백을 기준으로 split
  for char in words:
      answer += morse[char]
  
  return answer


# 점 위치
def solution(dot):
  answer = 0

  if dot[0] > 0:
    if dot[1] > 0:
      answer = 1
    else:
      answer = 4
  if dot[0] < 0:
    if dot[1] > 0:
      answer = 2
    else:
      answer = 3

  return answer


# 구슬나누기
import math
def solution(balls, share):
  answer = 0

  balls_fac = math.factorial(balls)
  share_fac = math.factorial(share)
  bmins_fac = math.factorial(balls - share)

  answer = int(balls_fac / (share_fac * bmins_fac))
  
  return answer


# 2차원
def solution(num_list, n):
  answer = []

  for i in range(0, len(num_list), n):
    answer.append(num_list[i:i+n])

  return answer


# 배열회전
def solution(numbers, direction):
  answer = []
  if direction == 'right':
    answer = [numbers[-1]] + numbers[0:-1]
  elif direction == 'left':
    answer = numbers[1:] + [numbers[0]]
    
  return answer
# print(solution( [1, 2, 3], 'right' ))


# 공던지기
def solution(numbers, k):
  answer = 0
  nlen = len(numbers)
  idx = 0

  idx = ((k - 1) * 2) % nlen
  answer = numbers[idx]

  return answer
  
print(solution(	[1, 2, 3, 4, 5, 6], 2 ))