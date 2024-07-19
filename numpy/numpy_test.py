import numpy as np


arr= np.array([2,3,45,6])
# print(arr)
# print(type(arr))
# Create a 1D numpy array from a list
# arr = np.array([1, 2, 3, 4, 5])
arr = np.array((1,2,3,4,5))
# print(arr[0])
# print(arr[2] + arr[4])

# print(np.__version__)

a = np.array([1,2,3,4,5])
b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
c= np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[1,2,3,4,5],[6,7,8,9,10]]])
d= np.array([90])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

arr = np.array([1,2,3,4], ndmin=5)
# print(arr)
# print("number of dimension: ", arr.ndim)
# print("second element on first row: ", c[0,0,1])

# print(arr[0:2:4])
# print(b[1:1,2])

# arr = np.array(["Rohan","Rahul","Virat"])
new_arr = arr.view()
# new_arr = arr.copy()
arr[0] = 45
# print(arr)
# print(new_arr)

x= arr.view()
y= arr.copy()
# print(x.base)
# print(y.base)

# print(b.shape)
# print(arr.shape)


#Iteration on array

# for x in a:
    # print(x)

# for x in b:
#     print(x)

# for x in b:
#     for y in x:
#         print(y)

# for x in c:
#     for y in x:
#         print(y)

# for x in c:
#     for y in x:
#         for z in y:
#             print(z)

# The function nditer() solve the problem of iteration from using nloop for n dimension
# for x in np.nditer(c):
#     print(x)

# Joining numpy array

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1,arr2))
# print(arr)

arr1= np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
arr = np.concatenate((arr1,arr2 ) , axis= 1)

# Split is reverse of joining array we split array with the array_split

new_arr = np.array_split(arr,2)
# print(arr)
# print(new_arr)


# Searching the array using where
arr = np.array([1,2,3,4,2])
# x = np.where(arr ==2)
arr = np.array([1,2,3,4,5,6,7,8,10,12])
# x = np.where(arr %2 ==0) using this we have the indexes of the even number
# print(x)

# Sorting the array in order

arr = np.array([0,3,5,2,1])
arr = np.array(['banana','mango','apple'])
print(np.sort(arr))