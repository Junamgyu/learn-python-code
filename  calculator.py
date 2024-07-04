print("두 수를 계산하겠습니다.")
a = int(input("처음 수를 입력해 주세요 :"))
b = int(input("다음 수를 입력해 주세요 :"))

# 계산함수
def sum(a, b):       
    result = a + b     
    return result  

def min(a, b):
    result =  a - b
    return result

def mul(a, b):
    result = a * b
    return result

def div(a, b):
    result = a / b
    return result

print ("1. 덧셈")
print ("2. 뺄셈")
print ("3. 곱셈")
print ("4. 나눗셈")
count = int(input("계산할 부호를 정해주세요 :"))

#덧셈
if count == 1:
  print("덧셈을 하겠습니다.")
  print(sum(a, b))
#뺄셈
elif count == 2:
  print("뺄셈을 하겠습니다.")
  print(min(a, b))
#곱셈
elif count == 3:
  print("곱셈을 하겠습니다.")
  print(mul(a,b))
#나눗셈  
elif count == 4:
  print("나눗셈을 하겠습니다.")
  print(div(a,b))
else :
  print("잘못된 입력입니다.")