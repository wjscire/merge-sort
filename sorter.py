"""
Function: merge_sort
This function implements a recursive merge sorting algorithm.
A list of unsorted items is progressively broken down into
smaller sets until each set contains just one item. These sets
are then sorted and merged together with other sets in order
to completely order the original list.
Parameters:
    data | list -- A list of unsorted data.
Returns:
    None.
"""
def merge_sort(data: list) -> None:
    # Base-case. Return if the list is one item or less.
    if len(data) > 1:
        # Finding split point of list.
        mid = len(data)//2
        # Creating two sub-lists.
        left = data[:mid]
        right = data[mid:]
        # Recursively breaking down and sorting each sub-list.
        merge_sort(left)
        merge_sort(right)
        # Sorting indices.
        i = j = s = 0
        # Sort by appending the next smallest item from either sublist.
        while (i < len(left)) and (j < len(right)):
            if left[i] <= right[j]:
                data[s] = left[i]
                i += 1
            else:
                data[s] = right[j]
                j += 1
            s += 1
        # If one or the other sub-lists has remaining items, append them.
        while i < len(left):
            data[s] = left[i]
            i += 1
            s += 1
        while j < len(right):
            data[s] = right[j]
            j += 1
            s += 1
