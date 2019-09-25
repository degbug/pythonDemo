# -*- coding: utf-8 -*-
# 上面一行定义使用utf-8编码，否则运行文件中带中文报错
print("hello Python world!")

message="this is a message"
print(message)

# 单引号
message = 'this is a message "2" '
print(message)
## test中文
message="""
one
two
three
第四行
"""
print(message)

print(message.upper())
print(message.lower())
# 首字母大写
print(message.title())
print(message.translate)


print("begin")
favorite_language = '\n\t python \n\t'
#清除后面空白符
print(favorite_language.rstrip())
#清除前面的空白符
print(favorite_language.lstrip())
#清除两端空白符
print(favorite_language.strip())
print("end")