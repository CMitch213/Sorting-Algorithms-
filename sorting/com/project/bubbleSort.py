# Bubble sort

# Bubble sorting works by checking if the object to the left is bigger than the one to the right.
# If it is bigger it swaps the positions until it is fully sorted

def bubbleSort(array):
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                #swaps elements if they arent already sorted
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


data = [0, 9, 35, -69, 15]

bubbleSort(data)

print('The bubble have floated, the numbers are:')
print(data)