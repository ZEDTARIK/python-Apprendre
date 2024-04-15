def binary_search(arr, target):
    low = 0
    high = len(arr) -1 

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
    

if __name__ == "__main__":
    arr = range(1, 100_000_000_000_000_001)
    print("found in index :", binary_search(arr, 6))
    print("found in index :", binary_search(arr, 415487))
    
    print("found in index :", binary_search(arr, 100_000_000_000_000_000))