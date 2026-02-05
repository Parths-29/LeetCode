#readme - so in this question the proivded things are  - You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules:

#For each index i (where 0 <= i < nums.length), perform the following independent actions:
#if nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value of the index where you land.
#If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value of the index where you land.
#If nums[i] == 0: Set result[i] to nums[i].
#Return the new array result. 
# so my approach for this i gonna be - the array is circluar so movement is gonna be mod with the length of the array and also we need to take care of negative movement as well so we can add the length of the array to the negative movement to get the correct index. will get wrap then 
#Create a result array of the same size.
#Traverse aeach index i in nums.
#If nums[i] is zero, store 0 in result.
##therwise move nums[i] steps from index i.
#Use (i + nums[i]) % n to handle circular movement.
#Store the value at the computed index in result.
# so my code  = 
def transformedArray(nums):
    n = len(nums)
    result = [0] * n

    for i in range(n):
        if nums[i] == 0:
            result[i] = 0
        else:
            new_index = (i + nums[i]) % n
            result[i] = nums[new_index]

    return result
nums = list(map(int, input("Enter array elements: ").split()))
print("Transformed Array:", transformedArray(nums))
