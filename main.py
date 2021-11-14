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








#dupZeros([8, 4, 5, 0, 0, 0, 0, 7])
mergeArrays([1,2,3,0,0,0],[2,5,6,7])