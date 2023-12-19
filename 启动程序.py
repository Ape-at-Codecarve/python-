import new_version_spider
from time import sleep
a = input('输入西瓜作者的url\n>>>')
b = input('从作者的第几个视频爬起？\n(注：已10个视频为一个单位，例如，如果要从第221个视频开始爬起，则输入23，要从第一个视频开始爬输入1即可)\n>>>')
d = input('到哪里结束？\n(同样以10个视频为单位，例如，爬到第330个视频结束，则输入33)\n>>>')
d = int(d)
b = int(b)
c = input('输入倒计时(秒)\n>>>')
c = int(c)

sleep(c)
print(f'红字率设定为{new_version_spider.redChar_rate},爬取过程要保持浏览器的激活状态')
for cishu in range(b,d+1):
    new_version_spider.start(a,(cishu*10)-9,cishu*10)
    print(f'第{cishu}组已完成')
