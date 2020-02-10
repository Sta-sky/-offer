def quick_sort(arr):
    llist = []
    rlist = []
    if len(arr) <= 1:
        return arr
    else:
        for i in arr[1:]:
            if arr[0] >= i:
                llist.append(i)

        for i in  arr[1:]:
            if arr[0] < i:
                rlist.append(i)
        arr = quick_sort(llist) + [arr[0]] + quick_sort(rlist)
        return arr