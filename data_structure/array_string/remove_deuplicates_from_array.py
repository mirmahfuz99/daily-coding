#Using new array

def remove_duplicates(nums):
    unique_nums = []

    unique_nums.append(nums[0])

    n = len(nums)
    for i in range(1,n):
        if nums[i] != nums[i-1]:
            unique_nums.append(nums[i])

    print(unique_nums);
    return len(unique_nums)        

remove_duplicates([0,1,1,2,3,4,4,5])



#Using list and set buildin function
def remove_duplicates(nums):
    unique_nums = list(set(nums))
    unique_nums.sort()
    return len(unique_nums)

print(remove_duplicates([0,1,1,2,3,4,4,5]))



#Find len of unique nums, without using extra array and checked if array is empty.
def remove_duplicates(nums):
    if not nums:
        current_index = 0
    if nums:
        n = len(nums)
        current_index = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                current_index += 1
    return current_index        

print(remove_duplicates([1,1,1,1,1,1.2,3]))