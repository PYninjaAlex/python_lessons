# a = int(input(" Введите число 1 "))
# b = int(input(" Введите число 2 "))
# if a % 2 == 0:
#     a = str(a)
#     b = str(b)
#     print(a + b)
# elif   b % 2 == 0:
#     a = str(a)
#     b = str(b)
#     print(a + b)
#
# else:
#     print(a + b)

# a = int(input(" Введите число "))
# b = int(a ** 0.5)
# if a == b ** 2:
#     c = int((b + 1) ** 2)
#     print(c)
# else:
#     print(-1)

# sum = 1
# n = int(input(" Введите число "))
# for i in range(1,n):
#     sum /= i
# print(sum / n)

# sum = 0
# n = int(input(" Введите число "))
# for i in range(n):
#     sum += i
# print(sum + n)


# a = 0
# n = int(input(" Введите число "))
# b = 1 + n
# for i in range(1,b):
#     a += i ** i
# print(a)




# n = int(input(" Введите число n "))
# sum = 0
# for i in range(1,n + 1):
#     if i % 2 == 0:
#         sum -= i ** i
#     else:
#         sum += i ** i
# print(sum)





# n = int(input(" Введите число n "))
# sum = 1
# i = 1
# while sum < n:
#     print(sum, end=" ")
#     sum = 2 ** i
#     i += 1



# n = int(input(" Введите число n "))
# a = n // 2
# i = 2
# while i <= a:
#     if n % i == 0:
#         print(0)
#         break
#     i += 1
# else:
#     print(1)




# a = int(input(" Введите число a "))
# b = int(input(" Введите число b "))
# s = 0
# for i in range(1,a + 1):
#     s += i ** b
# print(s)



# товары = []
# count = int(input(" Введите количество товаров списка "))
# for i in range(count):
#     товары.append(input(" Имя товара "))
# for a in товары:
#     print(a)





# n = int(input(' Введите количество элементов списка '))
# list1 = []
# for i in range(n):
#     a = int(input(f' Введите число {i + 1} '))
#     list1.append(a)
# b = 0
# for a in list1:
#     b += a
# f = b /  n
# print(f)




s = input(' Введите текст ')
res = ""
for i in range(len(s)):
    b = ord(s[i]) + 13
    if b > ord('z'):
        b -= 26
    b = chr(b)
    res += b

print(res)
