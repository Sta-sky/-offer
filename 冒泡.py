"""
冒泡排序：
从头遍历  用第一个数字比较其他的数字
值小的进行换位，遍历比较之后，一次进行第二个，第三个，第n个直至比较完成。
返回数组
"""
arr = [4, 5, 23, 4, 3, 12, 6, 43]


def sort(arr):
    # first = arr[0]
    for j in range(len(arr)):
        for i in range(j + 1, len(arr)):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


result = sort(arr)
print(result)




