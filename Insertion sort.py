print("insertion sort")
def insertionsort(arr):
    for i in range(1,len(arr)):
        KEY=arr[i]
        #move elements of arr[0].....arr[i-1]
        #greater than key moves to right of their current position
        j=i-1
        while j>=0 and KEY<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=KEY
arr=[4,5,3,7,2,8,0]
insertionsort(arr)
print("sorted arrey is :")
for i in range(len(arr)):
    print(arr[i])