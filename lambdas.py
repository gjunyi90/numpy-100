import math
import numpy as np

# def mul_by_num(num):
#     """
#     Returns a function that takes one argument and returns num
#     times that argument.
#     >>> x = mul_by_num(5)
#     >>> y = mul_by_num(2)
#     >>> x(3)
#     15
#     >>> y(-4)
#     -8
#     """
#     "*** YOUR CODE HERE ***"
#     return ______

# def square_root(x):
#     return math.sqrt(x)

square_root = lambda x: x**2

x2 = square_root(2)
print(x2)

sum = lambda *x: print(x)
print(sum(1,2,5,4,6,6,2))