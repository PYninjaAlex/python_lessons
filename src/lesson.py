# a = 5
# b = 10
# c = 500
# if a * b ** 2 == c:
#     print(1)
# else:
#     print(0)

# a = 10
# b = 5
# c = 1
# if a != c:
#     b = a
# if not a != b:
#     print(a)
# else:
#     print(c)

# a = input(" Введите pin-code ")
# if len(a) == 4:
#     if a.isdigit():
#         print(1)
#     else:
#         print(0)
# else:
#     print(0)

# a = input(" Введите строку ")
# b = a[::-1]
# if a == b:
#     print(1)
# else:
#     print(o)


# year = int(input(" Введите год "))
# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     print(1)
# else:
#     print(0)



# a = int(input(" Введите число 1 "))
# b = int(input(" Введите число 2 "))
# c = int(input(" Введите число 3 "))
# if a == b == c:
#     print(3)
# elif a == b or a == c or b == c:
#     print(2)
# else:
#     print(0)



# a = int(input(" Введите число 1 "))
# b = int(input(" Введите число 2 "))
# c = int(input(" Введите число 3 "))
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)


# a = int(input(" Введите year 1 "))
# b = int(input(" Введите  month 1 "))
# c = int(input(" Введите  day 1 "))
# v = int(input(" Введите  year 2 "))
# f = int(input(" Введите число month 2 "))
# g = int(input(" Введите число day 2 "))
# if a > v:
#     print(2)
# elif v > a:
#     print(1)
# elif b > f:
#     print(2)
# elif f > b:
#     print(1)
# elif c > g:
#     print(2)
# elif g > c:
#     print(1)
# else:
#     print(' Одинаковый возраст ')


# login = input(" Введите логин ")
# password = input(" Введите пароль ")
# mail = input(" Введите почту ")
# number = input(" Введите телефон ")
# if len(login) > 6 and len(password) > 6 and mail.count("@") == 1 and number[0:2] == "+7" and len(number) > 10:
#     print("Данные верны")
# else:
#     print("Где-то ошибка")





# a = int(input(" Введите число 1 "))
# b = int(input(" Введите число 2 "))
# num = 0
# for i in range(a,b + 1):
#     if i % 2 == 0:
#         num += i
# print(num)



# n = int(input(" n "))
# suma = 0
# for i in range(1, n + 1):
#     if i % 3 == 0:
#         suma += i
# print(suma)




# n = int(input(" Введите число n "))
# sum = 0
# for i in range(1,n):
#     sum += i * (i + 1)
# print(sum)




# n = int(input(" Введите число n "))
# sum = 0
# for i in range(1,n + 1):
#     if i % 2 == 0:
#         sum -= i ** i
#     else:
#         sum += i ** i
# print(sum)




