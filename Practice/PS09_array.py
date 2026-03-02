import numpy as np

arr=np.array([10,20,30,40,50])
print("Array elements are:",arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
print(np.zeros(5))
print(np.ones(8))
print("even numbers are:",np.arange(2,10,2))
print("odd numbers are:",np.arange(1,10,2))

n = int(input("enter the size:"))
ele = list(map(int,input("enter the elements:").split()))
print("array elements are:",np.array(ele))