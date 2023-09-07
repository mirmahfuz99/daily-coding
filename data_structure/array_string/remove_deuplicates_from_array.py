#1

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