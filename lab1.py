#QN.1:
numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("Unique elements are:")
for num in unique_numbers:
    print(num)



#QN.2:
numbers = (12, 45, 3, 67, 23, 89, 34, 22, 10, 5)
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))



#QN.3:
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for x in list:
    if x % 2 == 0:
        even_numbers.append(x)
print(even_numbers)



#QN.4:
s = "hello world"
d = {}
for c in s:
    d[c] = d.get(c, 0) + 1
print(d)



#QN.5:
primes = set()
for num in range(2, 50):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.add(num)
n = int(input())
print(n in primes)


#QN.6:
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(list(set(a) & set(b)))


#QN.7:
a = {'x': 5, 'y': 10}
b = {'y': 3, 'z': 8}
c = {k: a.get(k, 0) + b.get(k, 0) for k in set(a) | set(b)}
print(c)


#QN.8:
names = ["sita", "hari", "sita", "Eve", "hari"]
d = {}
for name in names:
    d[name] = d.get(name, 0) + 1
print(d)


#QN.9:
a = [1, 2, 3, 4, 5]
b = [2, 4]
c = [x for x in a if x not in b]
print(c)


#QN.10:
d = {}
n = int(input())
for _ in range(n):
    k = input()
    v = input()
    d[k] = v
s = input()
print(d.get(s, "Not found"))


#CONDITIONS AND LOOP:

#QN.1:
n = int(input())
f = True
if n < 2:
    f = False
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        f = False
print("Prime" if f else "Not prime")


#QN.2:
for i in range(2, 101, 2):
    print(i)


#QN,3:
n = int(input())
f = 1
while n > 0:
    f *= n
    n -= 1
print(f)


#QN.4:
n = int(input())
for i in range(1, 11):
    print(n, '*', i, '=', n * i)


#QN.5:
a = list(map(int, input().split()))
print(max(a))
print(min(a))


#QN.6:
p = n = z = 0
for _ in range(10):
    x = int(input())
    if x > 0:
        p += 1
    elif x < 0:
        n += 1
    else:
        z += 1
print(p, n, z)


#QN.7:
n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b

#QN.8:
n = input()
print("Palindrome" if n == n[::-1] else "Not palindrome")


#QN.9:
for n in range(100, 1000):
    s = sum(int(d)**3 for d in str(n))
    if n == s:
        print(n)

#QN.10:
a = int(input())
b = int(input())
op = input()
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b != 0:
        print(a / b)
    else:
        print("Error")