# Some numbers have funny properties. For example:

# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

# In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that :

# ...

# If it is the case we will return k, if not return -1.

# Note: n and p will always be strictly positive integers.


# ------------------- MY SOLUTION: ------------------------------

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
    
# -------------------- best practices, for example: ----------------------------

def dig_pow(n, p):
    sum = 0
    for c in str(n):
        sum += int(c) ** p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1