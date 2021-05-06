import time
import random
import hashlib
import json


sha256=hashlib.sha256()

c=str(int(time.time() * 1000))   #13位时间戳
a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
h=''.join(random.choice(a) for i in range(16))   #随机16个字符
d='$d6eb7ff91ee257475%'   #默认值
e='2'       #最新信息为2
u='10'      #每页数量
page=str(1)   #页码
########
ts=c
rs=h
bb=[d,u,c,e,page,h]
bb.sort()
signature=hashlib.sha256((''.join(bb)).encode('utf-8')).hexdigest()
print(ts,rs,signature)

import requests

url = "https://tousu.sina.com.cn/api/index/feed?ts={}&rs={}&signature={}&type=2&page_size=10&page=1&_={}".format(ts,rs,signature,ts)
response = requests.request("GET", url)
print(json.loads(response.text))
