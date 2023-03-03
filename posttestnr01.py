import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in arr[1:]:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left) + [pivot] + quick_sort(right)

# Contoh penggunaan
my_list = [random.randint(0, 100) for i in range(10)]
print("Sebelum diurutkan:", my_list)
sorted_list = quick_sort(my_list)
print("Setelah diurutkan:", sorted_list)