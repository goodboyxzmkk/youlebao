# 1.创建一个列表
list1 = ['1', '2', '3', '4']
list2 = list("1234")
print(list1, list2)
print(list1 == list2)
# 以上创建的两个列表是等价的,都是['1', '2', '3', '4']

# 2.添加新元素
# 末尾追加
a = [1, 2, 3, 4, 5]
a.append(6)
print(a)

# 指定位置的前面插入一个元素
a.insert(2, 100)  # 在下标为2的前面插入一个元素100
print(a)

# 扩展列表list.extend(iterable),在一个列表上追加一个列表
a.extend([10, 11, 12])
print(a)

# 3.遍历列表
# 直接遍历
for i in a:
    print(i)

# 带索引的遍历列表
for index, i in enumerate(a):
    print(i, index)

# 4.访问列表中的值,直接通过下标取值.list[index]
print(a[2])

# 从list删除元素
# List.remove() 删除方式1:参数object 如果重复元素,只会删除最靠前的.
a = [1, 2, 3]
a.remove(2)  # 返回值是None

# List.pop()  删除方式2:pop 可选参数index,删除指定位置的元素 默认为最后一个元素
a = [1, 2, 3, 4, 5]
a.pop()
print(a)

a.pop(2)
print(a)

# 终极删除,可以删除列表或指定元素或者列表切片,list删除后无法访问
a = [1, 2, 3, 4, 5, 6]
del a[1]
print(a)  # 1, 3, 4, 5, 6]

del a[1:]
print(a)  # 1

del a
# print(a) # 出错,name a is not defined


# 排序和反转代码
# reverse 反转列表
a = [1, 2, 3, 4, 5]
a.reverse()
print(a)

# sort 对列表进行排序,默认升序排列.有三个默认参数cmp = None,key = None,reverse = False

# 7.Python的列表的截取与字符串操作类型相同,如下所示
L = ['spam', 'Spam', 'SPAM!']
print(L[-1])  # ['SPAM']

# 8.Python列表操作的函数和方法
len(a)  # 列表元素的个数
max(a)  # 返回列表元素最大值
min(a)  # 返回列表元素最小值
list(tuple)  # 将一个可迭代对象转换为列表

# 列表常用方法总结
a.append(4)
a.count(1)
a.extend([4, 5, 6])
a.index(3)
a.insert(0, 2)
a.remove(0)
a.pop()
a.reverse()
a.sort()
