# -*- coding: utf-8 -*-
import sys
print(sys.getdefaultencoding())

guests = ['xiaoming', 'zhangsan', 'lisi']

# 打印所有guest
print('所有嘉宾 : ' + str(guests))

print(guests[0] + "无法参加")

guests[0] = 'wangwu'


print('重新邀请' + guests[0] + '参加')

print("找到更大的桌子，可以邀请更多人了")

guests.insert(0, 'zhaoliu')
guests.insert(2, u"zhouliu")
guests.append(u'zhaoqi')
print(guests.pop())
print('all:' + str(guests))

