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


#dupZeros([8, 4, 5, 0, 0, 0, 0, 7])
#mergeArrays([1,2,3,0,0,0],[2,5,6,7])
#removeElement([0,1,2,2,3,0,4,2],2)
#removeElementDupes([0,0,1,1,1,2,2,3,3,4])
binarySearch([-1,0,3,5,9,12],9)