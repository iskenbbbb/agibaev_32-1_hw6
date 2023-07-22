def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(element, lst):
    pos = None
    first = 0
    last = len(lst) - 1

    while first <= last:
        middle = (first + last) // 2
        if lst[middle] == element:
            pos = middle
            break
        elif element > lst[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if pos is not None:
        print('Элемент найден.')
        print('Позиция элемента:', pos)
    else:
        print('Элемент не найден.')


input_list = [64, 34, 25, 12, 22, 11, 90]
listt = ['alma', 'bish', 'tash']

bubble_sort(input_list)
print(input_list)
binary_search('bish', listt)





input_list = [64, 34, 25, 12, 22, 11, 90]
listt = ['bish', 'alma', 'tash']



