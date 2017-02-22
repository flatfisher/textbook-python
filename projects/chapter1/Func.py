# -*- coding: utf-8 -*-

def do_calc(num1 = 0,num2 = 0):
    val1 = num1 + num2
    val2 = num1 - num2
    return val1,val2

value1,value2 = do_calc(6,2)
print(value1)
print(value2)