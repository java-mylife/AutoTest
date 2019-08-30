# coding:utf-8
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# '先取出100范围内的偶数，然后再把a加入到取出来的偶数中，然后组成一个list'
list_a = []

# def suanfa():
for i in range(0, 101):
    if i % 2 == 0:
        list_a.append(i)
# print list_a
list_b = []
list_b = a+list_a
# print len(list_b)
# print len(list_b)/2+1
list_c = []
list_c.append(list_b[31])
# print list_c
for i in range(0,len(list_b)/2+1):
    a = list_b[i]
    b = list_b[-(i+1)]
    c = a+b
    list_c.append(c)
print list_c

list1 = []
for i in range(1,10):
    for j in  range(i,10):
        a = i * j
        print '%s*%s=%s' % (i, j, a), " "
    print " "



# -*- coding:utf-8 -*-
for i in range(1,10):
    for j in range(1,i+1):
        print j,"*",i,"=",j*i," ",
    print("")


