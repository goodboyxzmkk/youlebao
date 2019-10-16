'''
#三元运算规则以及应用场景
aa = 0
bb = 2
res = aa if aa > 0 else bb

print(res)
'''

# # 1. 去掉空格和特殊符号
# name = " abcdefgeyameng  "
# name1 = name.strip()  # 并不会在原来的字符串上操作,返回一个去除了两边空白的字符串
# print(name1, len(name1), name, len(name))
# # abcdefgeyameng 14  abcdefgeyameng   17
#
# # 去掉左边的空格和换行符
# name2 = name.lstrip()
# print(name2, len(name2))# print(name2, len(name2))#
#
# # 去掉右边的空格和换行符
# name3 = name.rstrip()
# print(name3, len(name3)) # abcdefgeyameng 15


# 2.字符串的搜索和替换
# name = " abcdefgeyameng  "

# name.count('e')  # 查找某个字符在字符串中出现的次数
# name.capitalize()  # 首字母大写
# name.center(100, '-')  # 把字符串方中间,两边用-补齐,100表示占位多少
# name.find('a')  # 找到这个字符返回下标,多个时返回第一个,不存在时返回-1
# name.index('a')  # 找到这个字符返回下标,多个时返回第一个,不存在时报错
# print(name.replace(name, '123'))  # 字符串的替换
# name.replace('abc', '123')  # 注意字符串的替换的话,不是在原来的字符串上进行替换.而是返回一个替换后的字符串.

# 3.字符串的测试和替换函数
# name.startswith("abc")  # 是否以abc开头
# name.endswith("def")  # 是否以def结尾
# name.isalnum()  # 是否全是字母和数字,并且至少包含一个字符
# name.isalpha()  # 是否全是字母,并至少包含一个字符
# name.isdigit()  # 是否全是数字,并且至少包含一个字符
# name.isspace()  # 是否全是空白字符,并且至少包含一个字符
# name.islower()  # 是否全是小写
# name.isupper()  # 是否全是大写
# name.istitle()  # 是否是首字母大写

# # 4.字符串的分割
# name.split('') # 默认按照空格进行分隔,从前往后分隔
# name.rsplit() # 从后往前进行分隔
#
# 5.连接字符串
# str = '.'.join(name)  # 用.号将一个可迭代的序列拼接起来
# print(str)
name = '123456789'
# 6.截取字符串(切片)
name1 = name[0:3]  # 第一位到第三位的字符,和range一样不包含结尾索引
name2 = name[:]  # 截取全部的字符
name3 = name[6:]  # 截取第6个字符到结尾
name4 = name[:-3]  # 截取从开头到最后三个字符之前
name5 = name[-1]  # 截取最后一个字符
name6 = name[::-1]  # 创造一个与原字符串顺序相反的字符串
name7 = name[:-5:-1]  # 逆序截取
print(name1)
print(name2)
print(name3)
print(name4)
print(name5)
print(name6)
print(name7)
