def merge(lst1, lst2):
    index_lst1 = 0
    index_lst2 = 0
    index_result_lst = 0
    result_lst = []

    for i in range(len(lst1) + len(lst2)):
        result_lst.append(i)

    while((index_lst1<len(lst1)) and (index_lst2<len(lst2))):
        if(lst1[index_lst1] < lst2[index_lst2]):
            result_lst[index_result_lst] = lst1[index_lst1]
            index_result_lst += 1
            index_lst1 += 1
        else:
            result_lst[index_result_lst] = lst2[index_lst2]
            index_result_lst += 1
            index_lst2 += 1
    while(index_lst1 < len(lst1)):
        result_lst[index_result_lst] = lst1[index_lst1]
        index_result_lst += 1
        index_lst1 += 1
    while(index_lst2 < len(lst2)):
        result_lst[index_result_lst] = lst2[index_lst2]
        index_result_lst += 1
        index_lst2 += 1

    return result_lst

# Test code
# lst1 = [0, 5, 8, 9, 10, 13]
# lst2 = [4, 6, 7, 12, 14, 16, 20]

lst1 = [-5, -2, -1, 2, 8, 17, 21]
lst2 = [-6, -3, -1, 0, 7, 10, 11, 16, 20]

print(merge(lst1, lst2))
