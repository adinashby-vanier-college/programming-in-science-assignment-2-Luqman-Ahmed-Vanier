# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
  max1 = None
  max2 = None
  for num in numbers:
      if max1 == None or num > max1:
          max2 = max1 
          max1 = num
      elif num != max1 and (max2 == None or num > max2):
          max2 = num
  return max1, max2

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
  # Remove duplicates
  unique_numbers = []
  for num in numbers:
      if num not in unique_numbers:
          unique_numbers += [num]
          
  n = len(unique_numbers)
  for i in range(n):
      for j in range(0, n-i-1):
          if unique_numbers[j] > unique_numbers[j+1]:

              unique_numbers[j], unique_numbers[j+1] = unique_numbers[j+1], unique_numbers[j]
  return unique_numbers

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
  result = [0] * len(arr)  
  total = 0
  for i in range(len(arr)):
      total += arr[i]  
      result[i] = total  
  return result

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
  transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
  return transpose

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
  result = []
  for i in range(len(lst)):
      if i % step == 0:  
          result += [lst[i]]  
  return result

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
  result = 0
  for i in range(len(list1)):
      result += list1[i] * list2[i]
  return result

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
  rows1 = len(matrix1)
  cols1 = len(matrix1[0])
  rows2 = len(matrix2) 
  cols2 = len(matrix2[0])

  result = [[0] * cols1 for r in range(rows1)]

  for i in range(rows1): 
      for j in range(cols2):  
          total = 0
          for k in range(cols1): 
              total += matrix1[i][k] * matrix2[k][j]
          result[i][j] = total 
  return result