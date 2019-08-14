'''Find pair in array/list whose sum is closest to target in O(n) time
Time Complexity: O(n log n) + O(n) = O(n log n) because we are sorting the array by ourself.
If array is already sorted, we can remove line# 12, and the time complexity would be O(n)'''

max_num = 10000000000


def find_closest_pair(array, n, target):
    '''array - input array/list
       n - length of the array/list
       target - target sum '''
    array.sort()
    l, r = 0, n-1
    res_l, res_r = 0, 0
    diff = max_num

    while l < r:
        d = abs((array[l] + array[r]) - target)

        if d < diff:
            diff, res_l, res_r = d, l, r

        if (array[l] + array[r]) > target:
            r -= 1
        else:
            l += 1
    
    return array[res_l], array[res_r]
