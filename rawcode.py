def bubble_sort(lists):
    """
    实现冒泡排序
    Args:
        lists: list
            待排序的数组
    return 排好序的数组
    """
    length = len(lists)

    for i in range(0, length):
        did_swap = False

        for j in range(0, length - 1 - i):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
                did_swap = True

        if did_swap is False:
            return lists


# 测试
assert bubble_sort([3,1,0,12,3])==[0, 1, 3, 3, 12]
assert bubble_sort([0,34,1,4,1])==[0, 1, 1, 4, 34]