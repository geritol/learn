total = 0

def next_pivot(n):
    first = n[0]
    last = n[-1]
    median_index = len(n)//2
    if len(n) % 2 == 0: median_index -= 1
    median = n[median_index]
    # print(n)
    # print(median)
    return n.index(sorted([first, last, median])[1])


def quick_sort(array):
    global total
    length = len(array)
    if length <= 1: return array

    pivot_index = next_pivot(array)
    pivot = array[pivot_index]

    array[0], array[pivot_index] = pivot, array[0]
    divider = 0

    for i in range(1, length):
        current = array[i]
        if pivot > current:
            divider += 1
            if i == divider: continue
            array[divider], array[i] = current, array[divider]

    array[0], array[divider] = array[divider], pivot

    total += length-1

    return quick_sort(array[0:divider]) + [pivot] + quick_sort(array[divider+1:])

#test = [2,1,3,4, 6]
#test2 = [2,3,4,1]


#print(quick_sort(test))
#print(total)

#total = 0

import time
start = time.time()
with open('QuickSort.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [int(x.strip()) for x in content]
end = time.time()

print(end-start)
res = quick_sort(content)
print(res)
#print(total)