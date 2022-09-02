# i = number of sorting iterations
# j = iterator for list
# After every iteration the highest values settles down at the end of the array.
# Hence, the next iteration need not include already sorted elements.

def bubbleSort(lst):
    n = len(lst)

    # Flag to confirm if list is already sorted and no swaps are required
    swapped = False

    for i in range(n -1):
        for j in range(0, n -i -1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True

        # Exit when no swaps are required
        if not swapped:
            return
    return lst

lst = [90, 13, 27, 21, 35, 10]
print("Sorted List: " + str(bubbleSort(lst)))