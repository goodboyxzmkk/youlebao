# 正则表达式 提取数据

## 正则表达式

### 1. 正则表达式概念

# > ###### 正则表达式就是记录文本规则的代码

### 2. 正则表达式的样子

# > 0\d{2}-\d{8} 这个就是一个正则表达式，表达的意思是匹配的是座机号码

### 3. 正则表达式的特点

# - 正则表达式的语法很令人头疼，可读性差
# - 正则表达式通用行很强，能够适用于很多编程语言

## 1. re模块的使用过程

# 在Python中需要通过正则表达式对字符串进行匹配的时候，可以使用一个模块，名字为re
'''
    # 导入re模块
    import re

    # 使用match方法进行匹配操作
    result = re.match(正则表达式,要匹配的字符串)

    # 如果上一步匹配到数据的话，可以使用group方法来提取数据
    result.group()
'''

## 2. re模块示例

'''python
    #coding=utf-8

    import re

    result = re.match("hello","hello.cn")

    result.group()
'''
'''
运行结果为：

```
hello
'''

#### 定义

# > 用事先定义好的一些特定字符、及这些特定字符的组合，组成一个规则字符串，这个规则字符串用来表达对字符串的一种过滤逻辑。

#### 常见语法

# > 字符
#
# | 语法     | 说明                                                       | 表达式案例 | 完整匹配字符串    |
# | :------- | :--------------------------------------------------------- | :--------- | :---------------- |
# | 一般字符 | 匹配自身                                                   | abc        | abc               |
# | .        | 匹配任意除换行符`\n`外的字符。在DOTALL模式中也能匹配换行符 | a.c        | abc               |
# | \        | 转义字符，使后一个字符表示字符本身。                       | a.c        | a.c               |
# | [...]    | 选取字符范围                                               | a[bcd]e    | abe 或 ace 或 ade |
#
# > 预定义字符集（可以写在字符集[...]中）
#
# | 语法 | 说明                           | 表达式案例 | 完整匹配字符串 |
# | :--- | :----------------------------- | :--------- | :------------- |
# | \d   | 数字:[0-9]                     | a\dc       | a1c            |
# | \D   | 非数字:[^0-9]                  | a\Dc       | abc            |
# | \s   | 空白字符:[<空格>\t\r\n\f\v]    | a\sc       | a c            |
# | \S   | 非空白字符:[^<空格>\t\r\n\f\v] | a\Sc       | abc            |
# | \w   | 单词字符:[A-Za-z0-9_]          | a\wc       | abc            |
# | \W   | 非单词字符:[^A-Za-z0-9_]       | a\Wc       | a c            |
#
# > 数量词（用在字符或(...)之后）
#
# | 语法 | 说明                        | 表达式案例 | 完整匹配字符串 |
# | :--- | :-------------------------- | :--------- | :------------- |
# | *    | 匹配前一个字符0次或无限次。 | abc*       | abccc          |
# | +    | 匹配前一个字符1次或无限次。 | abc+       | abccc          |
# | ?    | 匹配前一个字符0次或1次。    | abc?       | abc 或 ab      |
# | {m}  | 匹配前一个字符m次。         | ab{2}c     | abbc           |

## 匹配单个字符


### 示例1：


# coding=utf-8

import re

ret = re.match(".", "M")
print(ret.group())

ret = re.match("t.o", "too")
print(ret.group())

ret = re.match("t.o", "two")
print(ret.group())

'''
运行结果：

M
too
two
'''

### 示例2：[]


import re

# 如果hello的首字符小写，那么正则表达式需要小写的h
ret = re.match("h", "hello Python")
print(ret.group())

# 如果hello的首字符大写，那么正则表达式需要大写的H
ret = re.match("H", "Hello Python")
print(ret.group())

# 大小写h都可以的情况
ret = re.match("[hH]", "hello Python")
print(ret.group())
ret = re.match("[hH]", "Hello Python")
print(ret.group())
ret = re.match("[hH]ello Python", "Hello Python")
print(ret.group())

# 匹配0到9第一种写法
ret = re.match("[0123456789]Hello Python", "7Hello Python")
print(ret.group())

# 匹配0到9第二种写法
ret = re.match("[0-9]Hello Python", "7Hello Python")
print(ret.group())

ret = re.match("[0-35-9]Hello Python", "7Hello Python")
print(ret.group())

# 下面这个正则不能够匹配到数字4，因此ret为None
ret = re.match("[0-35-9]Hello Python", "4Hello Python")
# print(ret.group())
'''

运行结果：

```python
h
H
h
H
Hello Python
7Hello Python
7Hello Python
7Hello Python
'''

### 示例3：\d


import re

# 普通的匹配方式
ret = re.match("嫦娥1号", "嫦娥1号发射成功")
print(ret.group())

ret = re.match("嫦娥2号", "嫦娥2号发射成功")
print(ret.group())

ret = re.match("嫦娥3号", "嫦娥3号发射成功")
print(ret.group())

# 使用\d进行匹配
ret = re.match("嫦娥\d号", "嫦娥1号发射成功")
print(ret.group())

ret = re.match("嫦娥\d号", "嫦娥2号发射成功")
print(ret.group())

ret = re.match("嫦娥\d号", "嫦娥3号发射成功")
print(ret.group())

'''
嫦娥1号
嫦娥2号
嫦娥3号
嫦娥1号
嫦娥2号
嫦娥3号
'''
### 示例4：\D


import re

match_obj = re.match("\D", "f")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")

'''
运行结果:

```python
f
'''

### 示例5：\s


import re

# 空格属于空白字符
match_obj = re.match("hello\sworld", "hello world")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

# \t 属于空白字符
match_obj = re.match("hello\sworld", "hello\tworld")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

'''
运行结果:

```python
hello world
hello world
'''

### 示例6：\S


import re

match_obj = re.match("hello\Sworld", "hello&world")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("hello\Sworld", "hello$world")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

'''
运行结果:

```python
hello&world
hello$world
'''

### 示例7：\w


import re

# 匹配非特殊字符中的一位
match_obj = re.match("\w", "A")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")

'''
执行结果:

```
A
'''

### 示例8：\W


# 匹配特殊字符中的一位
match_obj = re.match("\W", "&")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")

'''
执行结果:

```
&
'''

### 思考

# 匹配密码中的其中一位，密码是由字母、数字、下划线组成，请列举的方式匹配?

## 匹配多个字符

### 示例1：*

# 需求：匹配出一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可 有可无


import re

ret = re.match("[A-Z][a-z]*", "M")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "MnnM")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "Aabcdef")
print(ret.group())

'''
运行结果：

```python
M
Mnn
Aabcdef
'''

### 示例2：+

# 需求：匹配一个字符串，第一个字符是t,最后一个字符串是o,中间至少有一个字符

import re

match_obj = re.match("t.+o", "two")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

'''
运行结果：

```python
two
'''

### 示例3：?

# 需求：匹配出这样的数据，但是https 这个s可能有，也可能是http 这个s没有


import re

match_obj = re.match("https?", "http")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")
'''
运行结果：

```python
https
'''

### 示例4：{m}、{m,n}

# 需求：匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线


import re

ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
print(ret.group())

ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
print(ret.group())

'''
运行结果：

12a3g4
1ad12f23s34455ff66
'''

## 思考

# 如何使用正则表达式把qq:10567这样的数据匹配处理?

## 匹配开头和结尾

### 1. 匹配开头和结尾的正则表达式

# | 代码 | 功能           |
# | :--: | :------------- |
# |  ^   | 匹配字符串开头 |
# |  $   | 匹配字符串结尾 |

### 示例1：^

# 需求：匹配以数字开头的数据


import re

# 匹配以数字开头的数据
match_obj = re.match("^\d.*", "3hello")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")

'''
运行结果:

```python
3hello
'''

### 示例2：$

# 需求: 匹配以数字结尾的数据


import re

# 匹配以数字结尾的数据
match_obj = re.match(".*\d$", "hello5")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")

'''
运行结果：

```python
hello5
'''

### 示例3：^ 和 $

# 需求: 匹配以数字开头中间内容不管以数字结尾


match_obj = re.match("^\d.*\d$", "4hello4")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")

'''
运行结果:

```python
4hello4
'''

### 2.除了指定字符以外都匹配

# > ###### [^指定字符]: 表示除了指定字符都匹配

# 需求: 第一个字符除了aeiou的字符都匹配


import re

match_obj = re.match("[^aeiou]", "h")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")

'''
执行结果


h
'''

### 思考

# - 1.匹配以数字开头中间内容不管以数字结尾, 结尾不要4或者7
# - 2.匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
# - 3.匹配出11位手机号码
# - 4.匹配出微博中的话题, 比如: #幸福是奋斗出来的#

## 高级匹配


#### compile 方法

##### 作用

# 对正则表达式进行编译构建对象，后续不需要重新构建正则表达式上下文环境，从而提高效率

##### 使用方式


# 构建表达式对象
pattern = re.compile(r'表达式')
# 通过表达式对象对数据进行操作
# pattern.findall(string)


#### 贪婪模式和非贪婪模式区别

##### 贪婪模式

# - `(.*)` 尽可能多的匹配

##### 非贪婪模式

# - `(.*?)` 一旦匹配到就结束

#### DOTALL模式

# > `.`符号匹配所有的字符包括换行符


# !/usr/bin/python3
# -*- coding: utf-8 -*-

import re

string = '''
    abcd
    abcd
'''

# 相当于
# 1. 编译正则表达式
# (.*)      贪婪匹配，尽可能多匹配直到无法匹配
# (.*?)     非贪婪匹配，只要匹配到就返回
#  . 符号默认不包含换行符，DOTALL模式表示让 . 符号匹配任何字符包括换行符
# re.DOTALL == re.S == re.RegexFlag.DOTALL == re.RegexFlag.S
pattern = re.compile(r'a(.*)d', re.RegexFlag.S)

# 2. 提取数据
result = pattern.findall(string)
print(result)

#### 忽略大小写模式

# > 正则匹配时忽略大小写

# !/usr/bin/python3
# -*- coding: utf-8 -*-

import re

string = '''
    abcD
    abcD
'''

# 相当于
# 1. 编译正则表达式
# (.*)      贪婪匹配，尽可能多匹配直到无法匹配
# (.*?)     非贪婪匹配，只要匹配到就返回
#  . 符号默认不包含换行符，DOTALL模式表示让 . 符号匹配任何字符包括换行符
# re.DOTALL == re.S == re.RegexFlag.DOTALL == re.RegexFlag.S
# 忽略大小写
# re.IGNORECASE == re.I == re.RegexFlag.IGNORECASE == re.RegexFlag.I
# 忽略大小写并且支持 DOTALL模式 使用 |
pattern = re.compile(r'a(.*)d', re.RegexFlag.IGNORECASE | re.DOTALL)

# 2. 提取数据
result = pattern.findall(string)
print(result)

#### 原始字符串 r 的用法

# > 让字符串内部的转义字符没有任何意义。


# !/usr/bin/python3
# -*- coding: utf-8 -*-

string = r"abc\nd"
print(string)

#### 四大检索方法

# - **match** 开头匹配，只匹配一次
# - **search** 全局匹配，只匹配一次
# - **findall** 匹配所有符号条件的数据，返回是 结果列表
# - **finditer** 迭代对象，迭代 Match 对象

##### match 和 seach 区别

# > **match** 开头匹配，只匹配一次
# >
# > **search** 全局匹配，只匹配一次

##### findall 和 finditer 区别

# > **findall** 优点：使用简单，缺点：必须把所有数据搜索返回再返回
# >
# > **finditer** 优点：找到就返回，可以边找边返回
# >
# > 如果数据量小 使用 **findall**
# >
# > 如果数据量大 使用 **finditer**

##### 代码实现

# !/usr/bin/python3
# -*- coding: utf-8 -*-

import re

string = "123abc123"

# match 开头匹配，只匹配一次
pattern = re.compile('\d+')
# result = pattern.match(string)

# search 全局匹配，只匹配一次
# result = pattern.search(string)

'''
findall 优点：使用简单，缺点：必须把所有数据搜索返回再返回
finditer 优点：找到就返回，可以边找边返回
如果数据量小 使用 findall

如果数据量大 使用 finditer

'''
# findall 匹配所有符号条件的数据，返回是 结果列表
# result = pattern.findall(string)

# finditer 迭代对象，迭代 Match 对象
results = pattern.finditer(string)
for result in results:
    print(result)

print(results)

#### 分组与替换方法

##### 分组

# > 通过给定字符串进行对数据进行分组

# !/usr/bin/python3
# -*- coding: utf-8 -*-

import re

string = "a;dj jkl,jj; j;sd"
# split 分组
pattern = re.compile(r'[; ,]+')
result = pattern.split(string)
print(result)

##### 替换

# > 通过给定的正则表达式和替换字符进行替换
#

# !/usr/bin/python3
# -*- coding: utf-8 -*-

import re

# sub 交换
string = "hello world;sjd;ssdjkls;sdjk;crise lyj"
# 带 空格的词组替换成 #
pattern = re.compile(r'(\w+) (\w+)')

# 把 空格的词组 进行交换
result = pattern.sub(r"\2 \1", string)

print(result)

#### 常见提取方式

##### 使用流程

# 1. 拷贝原有字符串内容
# 2. 把所要提取的数据使用 `(.*)` 或 `(.*?)` 进行替换
# 3. 使用 `findall` 或 `finditer` 进行数据提取

##### 代码实现


# !/usr/bin/python3
# -*- coding: utf-8 -*-

import re

string = '<input type="submit" id="su" value="百度一下" class="bg s_btn">'

pattern = re.compile(r'<input type="submit" id="(.*?)" value="(.*?)" class="bg s_btn">')

result = pattern.findall(string)
print(result)
