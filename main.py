
def bubble_sort(arr):
    length = len(arr)
    arr_sorted = False
    while not arr_sorted:
        arr_sorted = True
        for xx in range(len(arr)-1):
            if arr[xx] > arr[xx + 1]:
                temp = arr[xx]
                arr[xx] = arr[xx+1]
                arr[xx+1] = temp
                arr_sorted = False
    print(arr)


if __name__ == '__main__':
    x = [1, 5, 2, 8, 11, 0, 3]
    bubble_sort(x)