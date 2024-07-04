def solution(a, b, flag):
    result = 0
    if flag == True:
        result = a + b
    #if flag == False:
    else: 
        result = a - b

    return result

result = solution(-4, 7, True)
print(result)

result = solution(-4, 7, False)
print(result)
