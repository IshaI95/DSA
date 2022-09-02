def insertion_sort(lst):
    for i in range(1, len(lst)):
        key_ele = lst[i]

        j = i-1

        # Move elements of lst[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j>=0 and lst[j] > key_ele:
            lst[j+1] = lst[j]
            j-=1

        lst[j+1] = key_ele
    return lst

# lst = [20, 10, 40, 6, 30]
# lst = [89, 19, 24, 0, 6, 15, 50, 48, 82]
lst = [-9, 13, -90, 70, 64, 23, 18, 76, 69, 0]
print("sorted list: " + str(insertion_sort(lst)))
