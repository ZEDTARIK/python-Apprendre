import time

def find_target_index(arr, target_value):
    """
    Searches for the target value in the given array and returns its index.
    If the target value is not found, returns -1.
    """
    low = 0
    high = len(arr) - 1

    start_time = time.time()

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target_value:
            end_time = time.time()
            print(f"Execution time: {end_time - start_time} seconds")
            return mid
        elif arr[mid] < target_value:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == "__main__":
    arr = range(1, 1_000_000_000_000)
    print(find_target_index(arr, 1954))