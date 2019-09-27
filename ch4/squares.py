# -*- coding:utf8 -*-
# 004

# 生成1，10的平方
# Python中两个星号（**）表示平方
squares = []
for value in range(1, 11):
    squares.append(value**2)

# 输出：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares)


# 对数字列表进行简单的统计计算
digits = list(range(1, 11))
# 输出1
print(min(digits))
# 输出10
print(max(digits))

# 输出55
print(sum(digits))

# 列表解析 将for循环和创建新元素的代码合并为一行，并自动附加新元素
squares = [value**2 for value in range(1,11)]
print(squares)
