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
        end_time = time.time()
        mid = (low + high) // 2

        if arr[mid] == target_value:
            
            print(f"Execution time: {format(end_time - start_time, ".2f")} seconds")
            return mid
        elif arr[mid] < target_value:
            low = mid + 1
            print(f"Execution time: {format(end_time - start_time, ".2f")} seconds")
        else:
            high = mid - 1
            print(f"Execution time: {format(end_time - start_time, ".2f")} seconds")

    return -1

if __name__ == "__main__":
    arr = range(1, 100_000_000_000_000)
    print("found in index :", find_target_index(arr, 6))
    print("found in index :", find_target_index(arr, 415487))