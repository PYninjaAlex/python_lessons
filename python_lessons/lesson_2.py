# a = int(input(" Введите число  a "))
# b = int(input(" Введите число  b "))
# while a <= b:
#     print(a, end=" ")
#     a += 1


# n = int(input(" Введите число n "))
# sum = 0
# for i in range(1,n + 1):
#     if i % 2 == 0:
#         sum -= i ** i
#     else:
#         sum += i ** i
# print(sum)




n = int(input(" Введите число n "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum)