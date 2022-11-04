#swap two numbers
# def swapTwoNumber(a, b):
#     a = a + b
#     b = a - b
#     a = a - b
#     return (a, b)
    
# print(swapTwoNumber(4, 5))

#method overloading

# def add(datatype, *args):
#     if datatype == 'int':
#         answer = 0
        
#     if datatype == 'str':
#         answer = ''
        
#     for x in args:
#         answer += x
        
#     return answer
    
# print(add('int', 5, 6))

#method overriding

# class A:
#     def test(self):
#         print("Function call from class A")
        
# class B(A):
#     def test(self):
#         print("Function call from class B")
        
# obj = A()
# obj_b = B()

# obj_b.test()

#second largest elemet in array
# def secondLargest(arr):
#     mx = max(arr[0], arr[1])
#     secondmx = min(arr[0], arr[1])
#     n = len(arr)
#     for i in range(2, n):
#         if(arr[i] > mx):
#             secondmx = mx
#             mx = arr[i]
#         elif(arr[i] > secondmx and mx != arr[i]):
#             secondmx = arr[i]
#         elif(secondmx == mx and secondmx != arr[i]):
#             secondmx = arr[i]
            
#     return secondmx
    
# print(secondLargest([7, 5, 2, 0, 61]))

#triplet question

# from itertools import combinations
# def findTriplet(arr):
#     result = []
#     possible_comb = combinations(arr, r=3)
#     for ele in possible_comb:
#         (i, j , k) = ele
#         if(i + j + k == 0):
#             result.append([i, j, k])
            
#     return result
        
    
# print(findTriplet([-1,0,1,2,-1,-4]))


#bubble sort
# def bubbleSort(arr):
#     n = len(arr)
    
#     swapped = False
#     for i in range(n-1):
#         for j in range(0, n-i-1):
#             if(arr[j]>arr[j+1]):
#                 swapped = True
#                 arr[j], arr[j+1] = arr[j + 1], arr[j]
                
#         if not swapped:
#             return
        
# arr = [7, 9, 3, 5, 7, 1, 0]
# bubbleSort(arr)
# print(arr)


# sum closest to zero
# def minSum(arr, arr_size):
#     inv_count = 0
#     if(arr_size < 2):
#         return
    
#     min_l = 0
#     min_r = 1
#     min_sum = arr[0] + arr[1]
#     for l in range(0, arr_size - 1):
#         for r in range(l + 1, arr_size):
#             sum_v = arr[l] + arr[r]
#             if(abs(min_sum) > abs(sum_v)):
#                 min_sum = sum_v
#                 min_l = l
#                 min_r = r
#     return arr[min_l], arr[min_r]
    
# print(minSum([-23, 12, -35, 45, 20, 36], 6))


        