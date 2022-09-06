# Problem Statement: Given a list and a number "k", find two numbers from the list that sum to "k".


def solve(lst, k):
    for i in range(len(lst)):
        for j in range(1, len(lst)):
            if lst[i] + lst[j] == k:
                return lst[i], lst[j]

lst = [-9, 1, 3, 8, 20, 29, 60, 5]
number = 32
print(solve(lst, number))