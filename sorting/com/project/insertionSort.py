# Insertion sort

# INsertion sort works by finding its location in the pattern, then moves to the next num.
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



arr = [0, 9, 35, -69, 15]
insertionSort(arr)
print("It has been inserted. The nums are:")
for i in range(len(arr)):
    print(arr[i])