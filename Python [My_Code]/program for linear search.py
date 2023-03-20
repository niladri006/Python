def linearSearch(arr, key):  #user-defined function
    for i in range(len(arr)): 
        if (arr[i] == key): 
            return i 
    return -1

arr = input('Enter the array of numbers: ')
arr = arr.split()
arr = [int(x) for x in arr]  
key = int(input('Enter number to search: '))  

index = linearSearch(arr, key) #calling function

if (index == -1):
    print(key, 'not Found.')
else:
    print(key, 'Found at Index', index)
