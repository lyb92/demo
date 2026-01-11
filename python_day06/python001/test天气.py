# coding:utf-8
import requests
import re

url = "http://www.weather.com.cn/weather1d/101010100.shtml"

# 反爬
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
resp = requests.get(url, headers=headers)  # resp相应结果对象
# 设置响应的编码格式
resp.encoding = 'utf-8'
# print(resp.text)
city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>', resp.text)
weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>', resp.text)
wd = re.findall('<span class="wd">(.*)</span>', resp.text)
zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>', resp.text)
# print(city)
# print(weather)
# print(wd)
# print(zs)
lst = []
for a, b, c, d in zip(city, weather, wd, zs):
    lst.append([a, b, c, d])
for item in lst:
    print(item)