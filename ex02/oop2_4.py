def factorials(n: int):
    result_dict = {}
    factorial = 1

    for num in range(1, n + 1):
        factorial *= num
        result_dict[num] = factorial

    return result_dict

k = factorials(5)
print(k[1])  
print(k[3]) 
print(k[5])  
