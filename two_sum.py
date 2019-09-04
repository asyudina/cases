#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
def twoSum(nums: List[int], target: int):

    lst = []
    for el in range(len(nums)):
        for elem in range(el+1,len(nums)):
            if nums[el] + nums[elem] == target:
                lst.append(el)
                lst.append(elem)
        if lst==[]:
            continue
        else: 
            break

    return lst

