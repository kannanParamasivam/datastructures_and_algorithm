
def find_closest_two_sum(nums1, nums2, target):
    l, r, diff, res_l, res_r = 0, len(nums2)-1, 10000000, 0, 0

    while l >= 0 and l < len(nums1) and r >= 0 and r < len(nums2):
        d = abs((nums1[l] + nums2[r])-target)

        if d < diff:
            diff = d
            res_l = l
            res_r = r

        if (nums1[l]+nums2[r]) > target:
            r -= 1
        else:
            l += 1

    return nums1[res_l], nums2[res_r]
