#!/usr/bin/python3
import calculator_1 as cal1
a=10
b=5
result1=cal1.add(a, b)
result2=cal1.sub(a, b)
result3=cal1.mul(a, b)
result4=cal1.div(a, b)
print(f"{a} + {b} = {result1}")
print(f"{a} - {b} = {result2}")
print(f"{a} * {b} = {result3}")
print(f"{a} / {b} = {result4}")