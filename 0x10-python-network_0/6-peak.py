#!/usr/bin/python3
"""Module with function for finding peak in list of unsorted ints"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    left, right = 0, len(list_of_integers) - 1
    nums = list_of_integers[:]

    if len(nums) == 0:
        return None
    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return nums[left]
