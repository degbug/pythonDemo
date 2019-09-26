# -*- coding: utf-8 -*-
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
# 修改值
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles[0] = "honda"

# 末尾添加值
motorcycles.append("ducati")
print(motorcycles)

# 在指定位置插入
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 删除元素
del motorcycles[0]
print(motorcycles)

# 移除末尾元素
motorcycles.pop()
print(motorcycles)

# 移除指定位置元素
motorcycles.pop(0)
print(motorcycles)

# 根据值删除元素
motorcycles.remove('yamaha')
print(motorcycles)