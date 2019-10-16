import time
import datetime

# print(time.asctime())      # 返回时间格式：Sun May  7 21:46:15 2017
# print(time.time())         # 返回时间戳 ‘1494164954.6677325’
# print(time.gmtime())       # 返回本地时间 的struct time对象格式，time.struct_time(tm_year=2017, tm_mon=5, tm_mday=7, tm_hour=22, tm_min=4, tm_sec=53, tm_wday=6, tm_yday=127, tm_isdst=0)
# print(time.localtime())    # 返回本地时间 的struct time对象格式，time.struct_time(tm_year=2017, tm_mon=5, tm_mday=7, tm_hour=22, tm_min=4, tm_sec=53, tm_wday=6, tm_yday=127, tm_isdst=0)
# print(time.gmtime(time.time()-800000))   # 返回utc时间的struc时间对象格式
# print(time.asctime(time.localtime()))    # 返回时间格式Sun May  7 22:15:09 2017
# print(time.ctime())                      # 返回时间格式Sun May  7 22:15:09 2017
# print(time.strftime('%Y-%m-%d'))         #默认当前时间 2017-05-07
# print(time.strftime('%Y-%m-%d',time.localtime())) #默认当前时间 2017-05-07

string_struct = time.strptime("2016/05/22", "%Y/%m/%d")  # 将日期字符串 转成 struct时间对象格式
print(
    string_struct)  # 返回struct time对象格式 time.struct_time(tm_year=2016, tm_mon=5, tm_mday=22, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=143, tm_isdst=-1)

# 将日期字符串转成时间戳
struct_stamp = time.mktime(string_struct)  # 将struct time时间对象转成时间戳
print(struct_stamp)  # 返回时间戳 ‘1463846400.0’

# 将时间戳转为字符串格式
print(time.gmtime(time.time() - 86640))  # 将utc时间戳转换成struct_time格式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))  # 将utc struct_time格式转成指定的字符串格式

# 时间加减
print(datetime.datetime.now())  # 返回当前时间 2017-05-07 22:36:45.179732
print(datetime.date.fromtimestamp(time.time()))  # 时间戳直接转换成日期格式 2017-05-07
print(datetime.datetime.now() + datetime.timedelta(3))  # 返回时间在当前日期上 +3 天
print(datetime.datetime.now() + datetime.timedelta(-3))  # 返回时间在当前日期上 -3 天
print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 返回时间在当前时间上 +3 小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))  # 返回时间在当前时间上 +30 分钟

c_time = datetime.datetime.now()
print(c_time)  # 当前时间为 2017-05-07 22:52:44.016732
print(c_time.replace(minute=3, hour=2))  # 时间替换 替换时间为‘2017-05-07 02:03:18.181732’

print(datetime.timedelta)  # 表示时间间隔，即两个时间点之间的长度
print(datetime.datetime.now() - datetime.timedelta(days=5))  # 返回时间在当前时间上 -5 天

# python 日历模块
import calendar

print(calendar.calendar(theyear=2017))  # 返回2017年整年日历
print(calendar.month(2017, 5))  # 返回某年某月的日历，返回类型为字符串类型

calendar.setfirstweekday(calendar.WEDNESDAY)  # 设置日历的第一天(第一天以星期三开始）
cal = calendar.month(2017, 4)
print(cal)

print(calendar.monthrange(2017, 5))  # 返回某个月的第一天和这个月的所有天数
print(calendar.monthcalendar(2017, 5))  # 返回某个月以每一周为元素的序列

cal = calendar.HTMLCalendar(calendar.MONDAY)
print(cal.formatmonth(2017, 5))  # 在html中打印某年某月的日历

print(calendar.isleap(2017))  # 判断是否为闰年
print(calendar.leapdays(2000, 2017))  # 判断两个年份间闰年的个数
