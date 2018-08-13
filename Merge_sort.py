# practice implementation of Merge sort from wikipedia: https://en.wikipedia.org/wiki/Merge_sort
def merge_sort(unsorted):
    print("unsorted = {0}".format(unsorted))

    # case when split is at the lowest level
    if len(unsorted) <= 1:
        return unsorted

    split_position = len(unsorted) // 2
    left_half = merge_sort(unsorted[:split_position])
    right_half = merge_sort(unsorted[split_position:])

    result = []
    left_index = 0
    right_index = 0
    # find the lowest value from left to right, starting with the left half
    while left_index < len(left_half):
        # case when the right half contained lower values than the left
        if right_index >= len(right_half):
            break

        # increase the index of left or right half until either is exhausted
        if left_half[left_index] < right_half[right_index]:
            result.append(left_half[left_index])
            left_index += 1
        else:
            result.append(right_half[right_index])
            right_index += 1

        print("appended = {0}".format(result))

    # case when there are left over values for left half
    if left_index < len(left_half):
        result.extend(left_half[left_index:])

    # case when there are left over values for right half
    if right_index < len(right_half):
        result.extend(right_half[right_index:])

    print("appended = {0}".format(result))
    return result


print("merge_sort: {0}".format(merge_sort([6, 5, 3, 1, 8, 7, 2, 4])))
