# -*- coding: utf-8 -*-
def normalize(name):
    a = name.lower()
    b = a.capitalize() 
    return b

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
