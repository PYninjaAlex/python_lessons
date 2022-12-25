# result = 0
# for temp in range(10):
#     if temp % 2 == 0:
#         result += 1
#     else:
#         result -= 1
# print(result)

# for i in range(5):
#     print(i)
#     print("hello")
#     i = i + 10
#     print(i,"Конец цикла")



# result = 0
# for temp in range(10):
#     if temp % 2 == 0:
#         result += 2
#     else:
#         result += 1
# print(result)




# a = int(input(" Введите число 1 "))
# b = int(input(" Введите число 2 "))
# for i in range(a,b + 1):
#     print(i,end=" ")






# a = 0
# for temp in range(5):
#     a += 1
#     if a == 3:
#         a += 2
#     if a == 4:
#         a += 3
#     if a == 5:
#         a += 4
#     else:
#         a += 1
# print(a)





# n = int(input(" Введите число n "))
# n1 = 0
# n2 = 1
# s = n1 + n2
# print(n2,n2, end=" ")
# while s < n:
#     n1,n2 = n2,s
#     s = n1 + n2
#     print(s, end=" ")




# n = int(input(" Введите число n "))
# x = float(input(" Введите число  x "))
# s = 1
# t = 1
# for i in range(1,n + 1):
#     t = t * x / i
#     s += t
# print(s)





# a = []
# n = 3
# for i in range(n):
#     a.append(input(" Введите число "))
# print(a[0],a[-1])



# a = int(input(" Введите число a "))
# b = []
# for i in range(a * 2 + 1):
#     if i % 2 != 0:
#         b.append(i)
# print(b)



# a = []
# n = 4
# for i in range(n):
#     a.append(int(input(" Введите число ")))
# print(int(sum(a) / n))





# var = 'python in skysmart'
# a = var.split("-")
# print(a)





# n = int(input(' Введите количество элементов списка '))
# list1 = []
# for i in range(n):
#     a = int(input(f' Введите число {i + 1} '))
#     list1.append(a)
# m = max(list1)
# print(m)




# n = int(input(' Введите количество элементов списка '))
# list1 = []
# for i in range(n):
#     a = int(input(f' Введите число {i + 1} '))
#     list1.append(a)
# list2 = []
# for a in list1:
#      if a % 2 == 1:
#          list2.append(a)
# b = min(list2) if len(list2) > 0 else 0
# print(b)



# n = int(input(' Введите количество элементов списка '))
# list1 = []
# for i in range(n):
#     a = int(input(f' Введите число {i + 1} '))
#     list1.append(a)
# count = 0
# for i in range (n - 1):
#     a = list1[i]
#     for j in range(i + 1,n):
#         if a == list1[j]:
#             count += 1
# print(count)





# n = input(' Введите число ')
# for i in range(len(n)-1):
#     a = int(n[i])
#     b = int(n[i + 1])
#     if abs(a - b ) != 1:
#         print(0)
#         break
# else:
#     print(1)



