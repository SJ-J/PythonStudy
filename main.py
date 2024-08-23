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


# 합성수찾기
def solution(n):
  answer = 0
  cnt = 0

  if n < 2:
    return 0

  for i in range(1, n + 1):  # 1~n
    cnt = 0
    for j in range(1, i + 1):  # 1~n의 약수 개수
        if i % j == 0:
          cnt += 1
    if cnt >= 3:
      answer += 1
    
  return answer


# 팩토리얼
def solution(n):
  answer = 1
  fac = 1

  if n > 3628800: return 0

  while fac <= n :
      answer += 1
      fac = fac * answer
  answer = answer-1
  
  return answer


# 최댓값만들기
def solution(numbers):
  answer = 0

  numbers.sort(reverse=True)
  answer = numbers[0] * numbers[1]
  
  return answer


# 주사위 개수 
def solution(box, n):
  answer = 0

  box_0 = int( box[0] / n )
  box_1 = int( box[1] / n )
  box_2 = int( box[2] / n )

  box = box_0 * box_1 * box_2
  answer = box
  
  return answer


# 모음 제거
def solution(my_string):
  answer = ''
  mo = ['a', 'e', 'i', 'o', 'u']
  for char in mo:
    my_string = my_string.replace(char, '')
    
  return my_string


# 문자열 정렬
def solution(my_string):
  answer = []
  nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

  for num in nums:
    answer += [int(char) for char in my_string if char == num]
    answer.sort()
    
  return answer


# 숨어있는 숫자의 덧셈1
def solution(my_string):
  answer = 0
  number = []
  nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  for num in nums:
    number += [int(char) for char in my_string if char == num]
    answer = sum(number)
  
  return answer


# 배열원소길이
def solution(strlist):
  answer = []

  for i in strlist:
    answer.append(len(i))
  
  return answer


# 중복문자제거
def solution(my_string):
  answer = ''
  dup = []
  
  for char in my_string:
    if char not in dup:
      dup.append(char)
      answer += char

  return answer


# 삼각형 완성 조건
def solution(sides):
  answer = 0
  maxnum = 0

  # 가능 1, 불가 2  
  maxnum = max(sides)

  sides.remove(maxnum)
  if sum(sides) > maxnum:
    answer = 1
  else:
    answer = 2

  return answer


# 소인수분해
def solution(n):
  answer = []
  p = 2        # 2부터 시작

  while p * p <= n:
    # p가 n의 소인수인 경우
    while n % p == 0:
      answer.append(p)
      n //= p
    p += 1

  if n > 1:
    answer.append(n)

  answer = list(set(answer))
  answer.sort()
  
  return answer
  

# 컨트롤제트
def solution(s):
  answer = 0

  s = s.split(" ")
  calc = []

  for i in s:                  # 공백 기준으로 자르기
      if i == 'Z':             # i가 Z인 경우
          if len(calc) != 0:   # calc가 비어있지 않은 경우
              calc.pop()       # 가장 최근에 확인한 값 pop
              print(calc)
      else:
          calc.append(int(i))  # i가 Z가 아닌 경우 calc 배열에 추가
          print(calc)

  answer = sum(calc)           # 빼지 않은 나머지 값 sum
  return answer


# 369
def solution(order):
  answer = 0
  nums = [int(digit) for digit in str(order)]

  for num in nums:
      if num in [3, 6, 9]:
          answer += 1

  return answer


# 암호해독
def solution(cipher, code):
  answer = ''
  sent = [str for str in cipher]  # 리스트에 담음

  for i, char in enumerate(sent, start=1):
    if i % code == 0:
        answer += char
  
  return answer


# 대문자와 소문자
def solution(my_string):
  answer = my_string.swapcase()
  return answer


# 가까운 수
def solution(array, n):

  array.sort()

  min_diff = float('inf')  # 설정한 가장 작은 값이 겹치는 경우를 대비하여 무한대로 초기값 설정
  answer = None

  for i in array:
      diff = abs(i - n)

      if diff < min_diff or (diff == min_diff and i < answer):
          min_diff = diff
          answer = i

  return answer


# 영어가 싫어요
def solution(numbers):
  answer = 0
  word = ''
  num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
  
  for char in numbers:
    word += char
    if word in num_dict:
      answer = answer * 10 + num_dict[word]
      word = ''
  
  return answer


# 약수 구하기
def solution(n):
  answer = []

  for i in range(1, n+1):
    if n % i == 0:
      answer.append(i)
  answer.sort()
  
  return answer


# 인덱스 바꾸기
def solution(my_string, num1, num2):
  answer = ''
  my_string = list(my_string)
  
  my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
  answer = ''.join(my_string)

  return answer


# 한 번만 등장한 문자
def solution(s):
  answer = ''
  seen = []
  only = []

  for char in s:
    if char not in seen:
      seen.append(char)
      only.append(char)
    elif char in only:
      only.remove(char)

    only.sort()
    answer = ''.join(only)

  return answer


# 편지
def solution(message):
  answer = 0
  return len(message) * 2


# 가장 큰 수
def solution(array):
  max_num = max(array)
  index_num = array.index(max_num)
  answer = [max_num, index_num]
  return answer


# 문자열 계산
def solution(my_string):
  calc = my_string.split(' ')
  answer = int(calc[0])
  for i in range(1, len(calc), 2):
    if calc[i] == '+':
      answer += int(calc[i + 1])
    elif calc[i] == '-':
      answer -= int(calc[i + 1])
  return answer


# 배열의 유사도
def solution(s1, s2):
  answer = 0
  set1 = set(s1)
  set2 = set(s2)
  answer = len(set1 & set2)
  return answer


print( solution( ["a", "b", "c"], ["com", "b", "d", "p", "c"] ) )



