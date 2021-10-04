# Code to merge two different sorted arrays
input_str1= input('Enter elements of the first array separated by space: ')
print("\n")
arr1 = input_str1.split()  # to convert the input string to list

print('array1: ', arr1)

input_str2= input('Enter elements of the second array separated by space: ')
print("\n")
arr2 = input_str2.split()  # to convert the input string to list

print('array2: ', arr2)

for i in range(len(arr1)):  # to convert each element to integer type
    arr1[i] = int(arr1[i])
for i in range(len(arr2)):  # to convert each element to integer type
    arr2[i] = int(arr2[i])


def mergeArrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    arr3 = [None] * (n1 + n2)
    i,j,k = 0,0,0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1
    while i < n1:
        arr3[k] = arr1[i];
        k = k + 1
        i = i + 1
    while j < n2:
        arr3[k] = arr2[j];
        k = k + 1
        j = j + 1
    for i in range(n1 + n2):
        print(str(arr3[i]), end = " ")


mergeArrays(arr1, arr2);
