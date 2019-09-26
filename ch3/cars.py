# -*- coding:utf8 -*-
cars = ['bmw','audi','toyota','subaru']

# 排序，会改变cars中对象的顺序
cars.sort()
print(cars)

# 逆序
cars.sort(reverse=True)
print(cars)

# sorted函数排序，返回一个排好序的集合
cars = ['bmw','audi','toyota','subaru']

print('\nsorted function:')
print(sorted(cars))
print(sorted(cars, reverse=True))
print(cars)

# 倒序
print('reverse function:')
cars.reverse()
print(cars)
cars.reverse()

# 确定列表的长度
print('cars length:' + str(len(cars)))

# 当要访问最后一个元素时可以使用-1这个索引
print('last element: ' + cars[-1])

# 循环
for car in cars:
    print(car)
