# -*- coding:utf8 -*-
# 002

# range函数生成一系列数值,如range(start,end),包括start，不包括end
# 如下代码输出1,2,3,4
for value in range(1,5):
    print(value)

# 使用list()将range()产生的结果转换为数值列表
numbers = list(range(1,5))
# 输出：[1, 2, 3, 4]
print(numbers)
