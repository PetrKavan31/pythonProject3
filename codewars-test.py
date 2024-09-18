def dig_pow(n, p):

    
    m = n
    sum_a = []
    while m != 0:
        y = m // 10
        z = m % 10
        m = y
        sum_a.append(z)
    sum_a.reverse()

    sum_b = 0
    for i in sum_a:
        a = i ** p
        p = p + 1
        sum_b = sum_b + a
    
    k = sum_b / n

    if k % 1 == 0:
        return k
    else:
        return -1
    
print(dig_pow(89,1))


