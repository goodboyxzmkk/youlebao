import os

print(os.getcwd())        # 获得当前工作目录
print(os.chdir("dirname")) # 改变当前脚本的工作路径，相当于shell下的cd
print(os.curdir)            # 返回当前目录‘.'
print(os.pardir)            # 获取当前目录的父目录字符串名‘..'
print(os.makedirs('dirname1/dirname2'))     # 可生成多层递归目录
print(os.removedirs('dirname1/dirname2'))      # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
print(os.mkdir('test4'))         # 生成单级目录；相当于shell中mkdir dirname
print(os.rmdir('test4'))        # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
print(os.listdir('/pythonStudy/s12/test'))   # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
print(os.remove('log.log'))            # 删除一个指定的文件
print(os.rename("oldname","newname"))    # 重命名文件/目录)
print(os.stat('/pythonStudy/s12/test'))     # 获取文件/目录信息
print(os.pathsep)            # 输出用于分割文件路径的字符串';'
print(os.name)               # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
print(os.system(command='bash'))   # 运行shell命令，直接显示
print(os.environ)                  # 获得系统的环境变量
print(os.path.abspath('/pythonStudy/s12/test'))   # 返回path规范化的绝对路径
print(os.path.split('/pythonStudy/s12/test'))     # 将path分割成目录和文件名二元组返回
print(os.path.dirname('/pythonStudy/s12/test'))    # 返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.basename('/pythonStudy/s12/test'))   # 返回path最后的文件名。如果path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.exists('test'))                 # 判断path是否存在
print(os.path.isabs('/pythonStudy/s12/test'))    # 如果path是绝对路径，返回True
print(os.path.isfile('test'))                   # 如果path是一个存在的文件，返回True。否则返回False
print(os.path.isdir('/pythonStudy/s12/test'))    # 如果path是一个存在的目录，则返回True。否则返回False
print(os.path.getatime('/pythonStudy/s12/test'))   # 返回path所指向的文件或者目录的最后存取时间
print(os.path.getmtime('/pythonStudy/s12/test'))   # 返回path所指向的文件或者目录的最后修改时间