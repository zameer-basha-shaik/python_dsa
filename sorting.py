#Selection Sort
def selection_sort(nums:list):
    for i in range(len(nums)-1):
        min = i
        for j in range(i,len(nums)):
            if nums[j] < nums[min]: min = j
        nums[i], nums[min] = nums[min], nums[i]
    return nums

#Bubble Sort
def bubble_sort(nums:list):
    for i in range(len(nums)-1, 0, -1):
        for j in range(0,i):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

#Insertion Sort
def insertion_sort(nums:list):
    n = len(nums)
    for i in range(n):
        j = i
        while j>0 and nums[j]<nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j-=1
    return nums
print(insertion_sort([1,11,1,23,4,5,52]))