# 使用时间库，将系统时间按照指定格式输出
import time
t = time.localtime()
print(time.strftime('%Y年%m月%d日%H时%M分%S秒',t))