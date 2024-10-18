def merge_sort(arr):
    """
    Sorts an array using the Merge Sort algorithm.

    Parameters:
    arr (list): A list of integers to be sorted.

    Returns:
    list: A sorted list of integers in non-decreasing order.
    """
    if len(arr) <= 1:
        return arr

    # Divide the array into halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])   # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two sorted lists into one sorted list.

    Parameters:
    left (list): The left sorted list.
    right (list): The right sorted list.

    Returns:
    list: A merged and sorted list of integers.
    """
    merged = []
    left_index, right_index = 0, 0

    # Compare each element and merge the two lists
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right list
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr)
    print("Sorted Output:", sorted_arr)
