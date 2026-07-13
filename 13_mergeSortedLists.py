# Merge two Sorted List

def merge(nums1, nums2):
    merged_list = []
    i, j = 0, 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged_list.append(nums1[i])
            i+=1
        else:
            merged_list.append(nums2[j])
            j+=1
    
    while i < len(nums1):
        merged_list.append(nums1[i])
        i+=1
    while j < len(nums2):
        merged_list.append(nums2[j])
        j+=1
        
    return merged_list

print(merge(nums1=[1,3,4,5], nums2=[2,6,8,9]))