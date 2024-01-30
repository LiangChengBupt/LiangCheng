DEBUG = True
# DEBUG = False
def printd(*args, **kwargs):
    if DEBUG:
        # 获取文件名（你可以根据需要修改文件名和路径）
        filename = '/mnt/data/airaiot/LiangCheng/debug_log.txt'
        
        # 将内容输出到控制台
        print(*args, **kwargs)
        
        # 将内容输出到文件
        with open(filename, 'a') as file:
            print(*args, file=file, **kwargs)
