import math


def dupZeros(arr):
    possible_dups = 0
    array_length = len(arr) - 1
    for count, x in enumerate(arr):
        if array_length - possible_dups <= count:
            break
        if x == 0:
            possible_dups += 1
        else:
            continue
    for x in range(array_length - possible_dups, -1, -1):
        if possible_dups == 0:
            break
        elif arr[x] == 0:
            arr[x + possible_dups] = arr[x]
            possible_dups -= 1
            arr[x + possible_dups] = arr[x]
        else:
            arr[x + possible_dups] = arr[x]

    print(arr)

def mergeArrays(nums1,nums2):
    for outer_value in nums2:
        if outer_value == 0:
            continue
        else:
            for count, inner_value in enumerate(nums1):
                if inner_value == 0:
                    nums1[count] = outer_value
                    break
                elif count >= len(nums1)-1:
                    nums1.append(outer_value)
                    break
    nums1.sort()

def removeElement(nums,val):
    k = 0
    for x in range(len(nums)-1,-1,-1):
        if x == len(nums)-1:
            if nums[x] == val:
                continue
            else:
                k += 1
        elif nums[x] == val:
            nums.append(nums[x])
            nums.remove(nums[x])
        else:
            k += 1
    print(k)

def removeElementDupes(nums):
    duped_values = []
    possible_deletes = 0
    for outer_value in nums:
        tester = outer_value in duped_values
        if not tester:
            duped_values.append(outer_value)
            possible_deletes = nums.count(outer_value) -1
            for x in range(len(nums)-1,-1,-1):
                if nums[x] == outer_value and possible_deletes > 0:
                    nums.append(nums[x])
                    nums.remove(nums[x])
                    possible_deletes -= 1
                else:
                    continue
        else:
            continue
    return len(duped_values)

def binarySearch(nums,target):
    left = 0
    right = len(nums) -1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            print(pivot)
            return pivot
        elif target < nums[pivot]:
            right = pivot -1
        else:
            left = pivot + 1
    print('Not in Array')

def numSquare(x):
        left = 0
        right = x // 2
        while left <= right:
            pivot = left + (right-left) // 2
            if pivot * pivot == x:
                print(pivot)
                return pivot
            if pivot * pivot > x:
                right = pivot - 1
            elif pivot * pivot < x:
                left = pivot + 1
        print(right)
        return right

def nonSortedBinary(nums,target):
    rotation_index = 0
    for x in range(0,len(nums)):
        if x == len(nums) - 1:
            break
        if nums[x] > nums[x+1]:
            rotation_index = x + 1
        else:
            continue
    #left side check
    left = 0
    right = rotation_index - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            print(pivot)
            return pivot
        elif nums[pivot] < target:
            left = pivot + 1
        elif nums[pivot] > target:
            right = pivot -1
    # right side check
    left = rotation_index
    right = len(nums)-1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            print(pivot)
            return pivot
        elif nums[pivot] < target:
            left = pivot + 1
        elif nums[pivot] > target:
            right = pivot - 1
    print('not in array')
    return -1

def checkDoubleExist(nums):
    for x in nums:
        for y in nums:
            if x * 2 == y:
                print('true')
                return True
            else:
                continue
    print('false')

def mountainArray(nums):
    nums_length = len(nums)
    i = 0
    if nums_length <= 2:
        print('not mountain array')
        return False
    while i+1 < nums_length and nums[i] < nums[i + 1]:
        i += 1
    if i == 0 or i == nums_length -1:
        print('not mountain array')
        return False
    while i +1 < nums_length and nums[i] > nums[i + 1]:
        i += 1

    if i == nums_length -1:
        print('This is a mountain array')
        return True
    else:
        print('not a mountain array')
        return False

def replaceGreatest(arr):

    mx = -1
    for i in range(len(arr) - 1, -1, -1):
        arr[i], mx = mx, max(arr[i], mx)
    return arr

def moveZeroes(nums):
    reading_pointer = 0
    for x in range(len(nums)):
        if nums[x] != 0 and nums[reading_pointer] == 0:
            nums[reading_pointer], nums[x] = nums[x], nums[reading_pointer]
        if nums[reading_pointer] != 0:
            reading_pointer += 1
    print(nums)


#dupZeros([8, 4, 5, 0, 0, 0, 0, 7])
#mergeArrays([1,2,3,0,0,0],[2,5,6,7])
#removeElement([0,1,2,2,3,0,4,2],2)
#removeElementDupes([0,0,1,1,1,2,2,3,3,4])
#binarySearch([-1,0,3,5,9,12],9)
#numSquare(500)
#nonSortedBinary([4,5,6,7,0,1,2],9)
#checkDoubleExist([-2,0,10,-19,4,6,-8])
#mountainArray([3,2,1,0])
#revist below, doing some cool assignments in python that I do not fully get right now
#replaceGreatest([17,18,5,4,6,1])
moveZeroes([0,1,0,3,12])