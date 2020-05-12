import sys

lst = []
for number in range(1, len(sys.argv)):
    if sys.argv[number].isdigit() is True:
        lst.append(int(sys.argv[number]))
    else:
        lst.append(sys.argv[number])

def insertion_sort(lst):
    for iteration in range(1, len(lst)):
        for position in range(iteration, 0, -1):
            if lst[position] < lst[position - 1]:
                swapper = lst[position - 1]
                lst[position - 1] = lst[position]
                lst[position] = swapper
            else:
                break
    return lst

print(insertion_sort(lst))