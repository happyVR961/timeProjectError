#import time 
# print(time.localtime(time.time()))
# print(time.asctime(time.localtime(time.time())))
# print(time.gmtime())
# print(time.localtime())
#print(time.strptime("25 Mar 21", "%d %b %y"))
import datetime
import time
import os
import shutil
x = time.strptime('18:58:15','%H:%M:%S')
path1 = "/Users/sumit/Downloads/abc/"
ctime = float(os.stat(path1).st_ctime)
result = datetime.timedelta(hours=ctime.tm_hour,minutes=ctime.tm_min,seconds=ctime.tm_sec).total_seconds()
print(result)
# def path():
#     if os.path.exists(path):
#         for root, dirs, files in os.walk(".", topDown = False):
#             #joinPath = os.path.join(root, path1)
#             ctime = os.stat(path1).st_ctime
#             return ctime
#         if(ctime>result):
#             os.remove(path1)
#         else:
#             shutil.rmtree(path1)
# path()

