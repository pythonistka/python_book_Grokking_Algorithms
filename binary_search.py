def binary_search(list, item):
    low = 0
    hight = len(list) - 1

    while low <= hight:
        mid = int((low + hight) / 2)
        answer = list[mid]
        if answer == item:
            return mid
        elif answer > item:
            hight = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9, 10, 12, 15, 77, 98]

print(binary_search(my_list, 98))
print(binary_search(my_list, 103))
print(binary_search(my_list, 1))