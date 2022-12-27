import time
from random import randint
def timer(func):
  def wrapper(arr):
    start = time.process_time()
    res = func(arr)
    end = time.process_time()
    print(f'{func.__name__}\n\t start: {start};\n end: {end};\n different: {end - start}')
    return res
  return wrapper



def findSmallest(arr):
    # Сохраняет наименьшее значение
  smallest = arr[0]
    # Сохраняет индекс наименьшего значения
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]
  return smallest_index

# Сортировка массива

@timer
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # Находит наименьший элемент в массиве и добавляет его в новый массив
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr

@timer
def quicksort(array):
  if len(array) < 2:
    # базовый случай, массивы с 0 или 1 элементом уже "отсортированы"
    return array
  else:
    # рекурсивный случай
    pivot = array[len(array) // 2] # индекс середины массива
    # подмассив всех элементов, меньших опорного
    less = [i for i in array[1:] if i <= pivot]
    # подмассив всех элементов больше, чем опорный
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


lst1 = [randint(0, 1000) for i in range(1000)]
lst2 = [randint(0, 1000) for i in range(1000)]

print(selectionSort(lst1),'\n\t',quicksort(lst2))
