def dig_pow(n, p):
   
   
   pass

m = 92
n = m
p = 1
print(n)
print(m)
sum_a = []
while n != 0:
   y = n // 10
   z = n % 10
   #a = z ** p
   n = y
   #p = p + 1
   sum_a.append(z)
   #print(x)
   print(z)
   #print(a)
sum_a.reverse()
print(sum_a)
sum_b = 0
for i in sum_a:
   a = i ** p
   p = p + 1
   print(a)
   sum_b = sum_b + a
print(sum_b)

c = sum_b / m
print(c)
print(c % 1)
if c % 1 == 0:
   print(c)
else:
   print(-1)