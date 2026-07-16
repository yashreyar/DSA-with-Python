'''
Each element in the result must be unique, and you may return the result in any order.

Input: nums1 = [1, 2, 3], nums2 = [4, 5, 6]
Output: []

Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2]
'''

def intersection(nums1, nums2):
    
    result = []
    for num in nums1:
        if num in nums2 and num not in result:
            result.append(num)
            
    return result

print(intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
