# coding:utf-8
# list = [1,2,3]
# if list[1]>list[0]:
#     list[0],list[1] = list[1],list[0]
# print list
'''ef bube_sort(lists):
    count = len(lists)
    for i in range(0,count):
        for j in range(i+1,count):
            if lists[i] > lists[j]:
                lists[i],lists[j] = lists[j],lists[i]
        print lists

# alist = [9,8,7,6,5,3,4]
print sorted(alist)
print bube_sort(alist)'''

'''def swap(x,i,j):
   """
   交换x的i,j位置元素
   """
   temp = x[i]
   x[i] = x[j]
   x[j] = temp
alist = [9,8,7,6,5,3,4]
def BubbleSort(x):
   j = len(x) - 1
   while j > 0:
       i = 0
       while i < j:
           if x[i] > x[i + 1]:
               swap(x,i,i+1)
           i += 1
       j -= 1
   return x
print BubbleSort(alist)'''


def bubbleSort(nums):
    for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):  # ｊ为列表下标
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [5,2,45,6,8,2,1]

print bubbleSort(nums)

def bubble_sort(list):
    count = len(list)
    for i in range(0,count):
        for j in range(i+1,count):
            if list[i]>list[j]:
                list[i],list[j] = list[j],list[i]
    return list
def bubbles_sort(list):
    for i in range(len(list)-1):
        for j in  range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list