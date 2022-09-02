def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i

        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

# lst = [64, 25, 12, 22, 11, 75, 9, 60, 13]
# lst = [89, 19, 24, 0, 6, 15, 50, 48, 82]

lst = [-9, 13, -90, 70, 64, 23, 18, 76, 69, 0]
print("Sorted List: " + str(selection_sort(lst)))