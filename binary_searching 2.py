def binary_Search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"found index: {binary_Search(arr, 9)}")
print(f"found index: {binary_Search(arr, 55)}")

names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah', 'Isaac']
target_name = 'Frank'
result_index = binary_Search(names, target_name)

if result_index != -1:
    print(f"Name '{target_name}' found at index {result_index}.")
else:
    print(f"Name '{target_name}' not found in the list.")
