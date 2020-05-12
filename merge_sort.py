import sys

lst = []
for number in range(1, len(sys.argv)):
    if sys.argv[number].isdigit() is True:
        lst.append(int(sys.argv[number]))
    else:
        lst.append(sys.argv[number])


def merge(left, right):
    merged_list = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged_list.append(right[right_index])
            right_index += 1
        else:
            merged_list.append(left[left_index])
            left_index += 1
    merged_list += left[left_index:]
    merged_list += right[right_index:]
    return merged_list


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    pointer = len(lst)//2
    left = merge_sort(lst[:pointer])
    right = merge_sort(lst[pointer:])
    return merge(left, right)

print(merge_sort(lst))