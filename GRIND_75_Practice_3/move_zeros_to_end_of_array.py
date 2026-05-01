from typing import List


def moveZerosToEnd(arr: List[int]) -> List[int]:
    l, r = 0, 1
    while r < len(arr):
        if arr[l] == 0:
            if arr[r] != 0:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r += 1
            else:
                r += 1
        else:
            l += 1
            r += 1

    return arr


# debug your code below
print(moveZerosToEnd([0, 1, 0, 3, 12]))
