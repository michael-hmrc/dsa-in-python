# Move backward with slow/fast pointers at the end.

def merge_sorted_arrays(nums1, m, nums2, n):
    write = m + n - 1
    i = m - 1
    j = n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[write] = nums1[i]
            i -= 1
        else:
            nums1[write] = nums2[j]
            j -= 1
        write -= 1

    while j >= 0:
        nums1[write] = nums2[j]
        write -= 1
        j -= 1
