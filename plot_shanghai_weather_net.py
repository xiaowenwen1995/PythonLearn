# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/2/23 21:53
@desc:
"""

import re
from datetime import datetime
from datetime import timedelta
from matplotlib import pyplot as plt
from urllib.request import *

def get_html(city, year, month):
    url = 'http://lishi.tianqi.com/'+city+'/'+str(year)+str(month)+'.html'
    request = Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36')
    response = urlopen(request)
    return response.read().decode('UTF-8')

dates, highs, lows = [],[],[]
city = 'shanghai'
year = '2019'
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
prev_day = datetime(2018, 12,31)

for month in months:
    html = get_html(city, year, month)
    text = "".join(html.split())
    # 匹配出天气数据表格
    patten = re.compile('<ulclass="lishitable_contentclearfix">(.*?)<liclass="lishitable_all">')
    table = re.findall(patten, text)
    # 匹配出表格行
    patten1 = re.compile('<li(.*?)</li>')
    uls = re.findall(patten1, table[0])
    for ul in uls:
        # 匹配出表格列
        patten2 = re.compile('>(.*?)</div>')
        lis = re.findall(patten2, ul)
        # 匹配出日期
        d_str = re.findall('">(.*?)</a>', lis[0])[0]
        try:
            cur_day = datetime.strptime(d_str, '%Y-%m-%d')
            high = int(lis[1])
            low = int(lis[2])
        except ValueError:
            print(cur_day, "数据出现错误")
        else:
            diff = cur_day - prev_day
            if diff != timedelta(days = 1):
                print('%s之前少了%d天的数据' % (cur_day, diff.days - 1))
            dates.append(cur_day)
            highs.append(high)
            lows.append(low)
            prev_day = cur_day

# 配置图形
fig = plt.figure(dpi=128, figsize=(12,9))
# 绘制最高气温
plt.plot(dates, highs, c='red', label='最高气温', alpha=0.5, linewidth=2.0)
# 绘制最低气温
plt.plot(dates, lows, c='blue', label='最低气温', alpha=0.5, linewidth=2.0)
# 填充颜色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 标题
plt.title("%s年上海最高气温和最低气温"% year)
# 坐标轴
plt.xlabel("日期")
fig.autofmt_xdate()
plt.ylabel("气温（℃）")
# 显示图例
plt.legend()
ax = plt.gca()
# 坐标轴颜色
ax.spines['right'].set_color("none")
ax.spines['top'].set_color("none")
plt.show()