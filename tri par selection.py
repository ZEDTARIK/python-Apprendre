import time

def selection_sort(arr):
    start_time = time.time()
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    end_time = time.time()
    print(f"Time taken for selection sort: {end_time - start_time} seconds")
    return arr

def test_selection_sort():
    # Test case 1: Sort a list of numbers in ascending order
    assert selection_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

    # Test case 2: Sort a list of numbers in ascending order
    assert selection_sort([7, 3, 5, 2, 8, 1, 4]) == [1, 2, 3, 4, 5, 7, 8]

    # Test case 3: Sort an empty list
    assert selection_sort([]) == []

    # Test case 4: Sort a list with a single number
    assert selection_sort([1]) == [1]

    # Test case 5: Sort a list with two numbers
    assert selection_sort([1, 2]) == [1, 2]

# Call the test function
test_selection_sort()