def dig_pow(n, p):    
    m = n
    numbers = []
    while m != 0:
        y = m // 10
        z = m % 10
        m = y
        numbers.append(z)
    numbers.reverse()

    sum_num = 0
    for i in numbers:
        a = i ** p
        p = p + 1
        sum_num = sum_num + a
    
    k = sum_num / n

    if k % 1 == 0:
        return k
    else:
        return -1
    
print(dig_pow(89,1))


