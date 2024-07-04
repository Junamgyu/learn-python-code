def solution(number, n, m):
    result = 0
    if number % n == 0:
        result = number % n
        if result % m == 0:
            result = 1
        else:
            result = 0
    else:
        result = 0
        
    return result

number = int(input("number 값을 입력하세요 : "))
n = int(input("n 값을 입력하세요 : "))
m = int(input("m 값을 입력하세요 : "))


print(solution(number, n, m))