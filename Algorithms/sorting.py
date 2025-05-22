def bubble_sort(arr):
    """
    This algo is based on pushing the greater elements to the right of the 
    array during each pass.
    Time Complexity: O(N)
    """
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def selection_sort(arr):
    """
    This algo is based on finding and setting the minimum element in the unsorted part of array.
    Time Complexity: O(N)
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr), 1):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insetion_sort(arr):
    return arr


if __name__ == "__main__":
    # print(bubble_sort([5,2,81,21,9,15]))
    # print(selection_sort([5,2,81,21,9,15]))
    print(insertion_sort([5,2,81,21,9,15]))