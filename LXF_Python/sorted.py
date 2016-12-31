# -*- coding: utf-8 -*-
#假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：

# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#!!!!!!!!!!!!!

def by_name(t):

    return t[0]

###return t[0] 即为 将 by_name 这个函数
###作用到 L 上的每个元素上 ， 并将元组的第一个数拿出来，以便排序
L2 = sorted(L, key=by_name)
print(L2)



#再按成绩从高到低排序：

# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
    return t[1]

L2 = sorted(L,key = by_score,reverse = True)
###reverse 为 True 则倒序排列 False 则正序
print(L2)