def bubble_sort(arr):
    a = arr[:]  # copy
    n = len(a)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

data = [5, 2, 9, 1, 7]
print("Before:", data)
print("After :", bubble_sort(data))
