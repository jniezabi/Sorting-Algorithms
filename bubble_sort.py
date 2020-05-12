import sys

lst = []
for number in range(1, len(sys.argv)):
    if sys.argv[number].isdigit() is True:
        lst.append(int(sys.argv[number]))
    else:
        lst.append(sys.argv[number])

def bubble_sort(lst):
    for iteration in range(len(lst) - 1, 0, -1):
        for position in range(iteration):
            if lst[position] > lst[position + 1]:
                swapper = lst[position]
                lst[position] = lst[position + 1]
                lst[position + 1] = swapper
    return lst

print(bubble_sort(lst))
