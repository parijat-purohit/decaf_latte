def count_numbers(sorted_list, less_than):
    l, h = 0, len(sorted_list) - 1

    if less_than <= sorted_list[0]:
        return 0
    elif less_than > sorted_list[-1]:
        return h+1

    while l <= h:
        mid = l + (h-l)//2
        if sorted_list[mid] == less_than:
            return mid
        elif sorted_list[mid] < less_than:
            if mid < len(sorted_list) - 1 and sorted_list[mid+1] >= less_than:
                return mid + 1
            else:
                l = mid + 1
        else:
            if mid > 0 and sorted_list[mid-1] < less_than:
                return mid
            else:
                h = mid - 1
    return mid


if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4))  # should print 2
