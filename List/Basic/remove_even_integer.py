def removeEvenInteger(lst):

    out_list = [n for n in lst if n % 2 != 0]
    return out_list

# validate
print(removeEvenInteger([-112, 169, 55, 80, 43, 90, 21]))